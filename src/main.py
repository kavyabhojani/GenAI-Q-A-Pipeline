import click

@click.command()
@click.option('--query', prompt='Enter your question', help='The question you want to ask.')
def main(query):
    print(f"Received query: {query}")
    print("This will soon fetch context from S3 and use a model to generate an answer.")

if __name__ == "__main__":
    main()
