import click
from src.logger import log_info, log_error
from src.s3_client import fetch_context
from src.bedrock_client import get_response_from_model
from src.validator import check_latency

@click.command()
@click.option('--query', prompt='Enter your question', help='The question you want to ask.')
def main(query):
    """
    Main CLI entry point for the GenAI Q&A Pipeline.
    1) Fetch context (simulated from S3)
    2) Generate response (simulated Bedrock call)
    3) Validate latency
    """
    log_info(f"Received query: {query}")

    try:
        context = fetch_context()
        log_info(f"Context loaded (length: {len(context)} characters)")
    except Exception as e:
        log_error(f"Failed to fetch context: {e}")
        return

    response, latency, within_limit = check_latency(get_response_from_model, query, context)

    log_info("Generated Response:")
    log_info(response)
    log_info(f"Latency: {latency:.4f} seconds")
    log_info(f"Within latency limit: {within_limit}")

if __name__ == "__main__":
    main()
