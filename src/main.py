import click
from src.logger import log_info, log_error
from src.s3_client import fetch_context
from src.bedrock_client import get_response_from_model
from src.validator import check_latency
from src.config import DEFAULT_MAX_LATENCY

@click.command()
@click.option('--query', prompt='Enter your question', help='The question you want to ask.')
@click.option('--max-latency', type=float, default=DEFAULT_MAX_LATENCY, show_default=True,
              help='Maximum allowed latency (seconds).')
@click.option('--show-context', is_flag=True, default=False, help='Print the loaded context.')
def main(query: str, max_latency: float, show_context: bool):
    log_info(f"Received query: {query}")

    try:
        context = fetch_context()
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

if __name__ == "__main__":
    main()
