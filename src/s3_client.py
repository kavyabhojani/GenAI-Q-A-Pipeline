from src.config import USE_REAL_S3, S3_BUCKET_NAME, CONTEXT_FILE_KEY
from src.logger import log_info, log_error

def fetch_context() -> str:
    try:
        if not USE_REAL_S3:
            log_info(f"[SIM] Fetching '{CONTEXT_FILE_KEY}' from '{S3_BUCKET_NAME}'")
            context = "Sample context text loaded from S3 (simulated)."
            log_info("[SIM] Context successfully fetched.")
            return context

        # Real S3 path (to be implemented when wiring boto3)
        # import boto3
        # s3 = boto3.client("s3")
        # obj = s3.get_object(Bucket=S3_BUCKET_NAME, Key=CONTEXT_FILE_KEY)
        # text = obj["Body"].read().decode("utf-8")
        # log_info("Context successfully fetched from S3.")
        # return text

        log_error("USE_REAL_S3=True but real S3 code not implemented yet.")
        return "ERROR: Real S3 path not implemented yet."
    except Exception as e:
        log_error(f"Failed to fetch context: {e}")
        raise
