import json
import click
from src.logger import log_info, log_error
from src.s3_client import fetch_context
from src.bedrock_client import get_response_from_model, pipeline_status
from src.validator import check_latency
from src.config import DEFAULT_MAX_LATENCY, S3_BUCKET_NAME, CONTEXT_FILE_KEY

APP_VERSION = "0.1.0"

@click.group()
def cli():
    pass

@cli.command(name="run")
@click.option('--query', prompt='Enter your question', help='The question you want to ask.')
@click.option('--max-latency', type=float, default=DEFAULT_MAX_LATENCY, show_default=True,
              help='Maximum allowed latency (seconds).')
@click.option('--show-context', is_flag=True, default=False, help='Print the loaded context.')
@click.option('--use-real-s3', is_flag=True, default=False, help='Fetch context from real S3 instead of simulation.')
@click.option('--bucket', default=S3_BUCKET_NAME, show_default=True, help='S3 bucket name (when using real S3).')
@click.option('--key', default=CONTEXT_FILE_KEY, show_default=True, help='S3 object key (when using real S3).')
@click.option('--json', 'as_json', is_flag=True, default=False, help='Output results as JSON.')
def run(query: str, max_latency: float, show_context: bool, use_real_s3: bool, bucket: str, key: str, as_json: bool):
    try:
        context = fetch_context(use_real_s3=use_real_s3, bucket_name=bucket, key=key)
    except Exception as e:
        if as_json:
            print(json.dumps({"ok": False, "error": f"Failed to fetch context: {e}"}))
        else:
            log_error(f"Failed to fetch context: {e}")
        return

    response, latency, within_limit = check_latency(
        get_response_from_model, query, context, max_latency=max_latency
    )

    if as_json:
        payload = {
            "ok": True,
            "query": query,
            "context_len": len(context),
            "used_real_s3": use_real_s3,
            "bucket": bucket if use_real_s3 else None,
            "key": key if use_real_s3 else None,
            "response": response,
            "latency_seconds": round(latency, 4),
            "within_latency_limit": within_limit,
            "max_latency_seconds": max_latency,
        }
        if show_context:
            payload["context"] = context
        print(json.dumps(payload, ensure_ascii=False))
        return

    log_info(f"Received query: {query}")
    if show_context:
        log_info(f"Context: {context}")
    else:
        log_info(f"Context loaded (length: {len(context)} characters)")
    log_info("Generated Response:")
    log_info(response)
    log_info(f"Latency: {latency:.4f} seconds (limit: {max_latency}s)")
    log_info(f"Within latency limit: {within_limit}")

@cli.command(name="health")
@click.option('--use-real-s3', is_flag=True, default=False, help='Check real S3 instead of simulation.')
@click.option('--bucket', default=S3_BUCKET_NAME, show_default=True, help='S3 bucket name (when using real S3).')
@click.option('--key', default=CONTEXT_FILE_KEY, show_default=True, help='S3 object key (when using real S3).')
@click.option('--json', 'as_json', is_flag=True, default=False, help='Output results as JSON.')
def health(use_real_s3: bool, bucket: str, key: str, as_json: bool):
    status = pipeline_status()
    try:
        context = fetch_context(use_real_s3=use_real_s3, bucket_name=bucket, key=key)
        s3_ok = True
        s3_msg = f"fetched {len(context)} chars from {bucket}/{key}" if use_real_s3 else "simulated fetch OK"
    except Exception as e:
        s3_ok = False
        s3_msg = f"ERROR: {e}"

    if as_json:
        print(json.dumps({
            "ok": s3_ok,
            "pipeline_status": status,
            "s3_ok": s3_ok,
            "s3_message": s3_msg,
            "used_real_s3": use_real_s3,
            "bucket": bucket if use_real_s3 else None,
            "key": key if use_real_s3 else None,
            "version": APP_VERSION,
        }))
        return

    log_info(f"Pipeline Status: {status}")
    if s3_ok:
        log_info(f"S3 Status: OK ({s3_msg})")
    else:
        log_error(f"S3 Status: {s3_msg}")

@cli.command(name="version")
def version():
    log_info(f"GenAI Q&A Pipeline - Version {APP_VERSION}")

if __name__ == "__main__":
    cli()
