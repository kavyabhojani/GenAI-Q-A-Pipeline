import click
from src.logger import log_info, log_error
from src.s3_client import fetch_context
from src.bedrock_client import get_response_from_model, pipeline_status
from src.validator import check_latency
from src.config import DEFAULT_MAX_LATENCY, S3_BUCKET_NAME, CONTEXT_FILE_KEY

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
def run(query: str, max_latency: float, show_context: bool, use_real_s3: bool, bucket: str, key: str):
    log_info(f"Received query: {query}")
    try:
        context = fetch_context(use_real_s3=use_real_s3, bucket_name=bucket, key=key)
        if show_context:
            log_info(f"Context: {context}")
        else:
            log_info(f"Context loaded (length: {len(context)} characters)")
    except Exception as e:
        log_error(f"Failed to fetch context: {e}")
        return

    response, latency, within_limit = check_latency(
        get_response_from_model, query, context, max_latency=max_latency
    )
    log_info("Generated Response:")
    log_info(response)
    log_info(f"Latency: {latency:.4f} seconds (limit: {max_latency}s)")
    log_info(f"Within latency limit: {within_limit}")

@cli.command(name="health")
@click.option('--use-real-s3', is_flag=True, default=False, help='Check real S3 instead of simulation.')
@click.option('--bucket', default=S3_BUCKET_NAME, show_default=True, help='S3 bucket name (when using real S3).')
@click.option('--key', default=CONTEXT_FILE_KEY, show_default=True, help='S3 object key (when using real S3).')
def health(use_real_s3: bool, bucket: str, key: str):
    log_info(f"Pipeline Status: {pipeline_status()}")
    try:
        context = fetch_context(use_real_s3=use_real_s3, bucket_name=bucket, key=key)
        log_info(f"S3 Status: OK (fetched {len(context)} chars from {bucket}/{key})")
    except Exception as e:
        log_error(f"S3 Status: ERROR ({e})")

if __name__ == "__main__":
    cli()
