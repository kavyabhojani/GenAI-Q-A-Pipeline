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
    print(f"\nReceived query: {query}")

    #fetch context
    context = fetch_context()
    print(f"Context loaded (length: {len(context)} characters)")

    #generate response and validate latency
    response, latency, within_limit = check_latency(get_response_from_model, query, context)

    #output results
    print("\nGenerated Response:")
    print(response)
    print(f"\nLatency: {latency:.4f} seconds")
    print(f"Within latency limit: {within_limit}")

if __name__ == "__main__":
    main()
