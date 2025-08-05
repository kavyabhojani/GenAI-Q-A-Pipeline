from src.config import S3_BUCKET_NAME, CONTEXT_FILE_KEY

def fetch_context():
    """
    Fetches context text from S3 bucket.
    Currently a placeholder – simulates retrieval.
    """
    print(f"Fetching {CONTEXT_FILE_KEY} from bucket {S3_BUCKET_NAME}")
    return "Sample context text loaded from S3 (simulated)."
