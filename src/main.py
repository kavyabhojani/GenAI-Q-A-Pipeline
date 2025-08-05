import click
from src.s3_client import fetch_context
from src.bedrock_client import get_response_from_model
from src.validator import check_latency


@click.command()
@click.option('--query', prompt='Enter your question', help='The question you want to ask.')
def main(query):
    """
    Main CLI entry point for the GenAI Q&A Pipeline.
    1. Fetch context (simulated from S3)
    2. Generate response (simulated Bedrock call)
    3. Validate latency
    """
    print(f"Received query: {query}")

    #fetch context
    context = fetch_context()
    print(f"Loaded context: {context}")

    #validate latency of model response
    response, latency, within_limit = check_latency(get_response_from_model, query, context)

    print(f"\nGenerated Response: {response}")
    print(f"Latency: {latency:.4f}s (Within limit: {within_limit})")


if __name__ == "__main__":
    main()
