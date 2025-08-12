from src.config import USE_REAL_S3, S3_BUCKET_NAME, CONTEXT_FILE_KEY
from src.logger import log_info, log_error

def fetch_context(use_real_s3: bool | None = None, bucket_name: str | None = None, key: str | None = None) -> str:
    real = USE_REAL_S3 if use_real_s3 is None else use_real_s3
    bucket = bucket_name or S3_BUCKET_NAME
    obj_key = key or CONTEXT_FILE_KEY

    if not real:
        log_info(f"[SIM] Fetching '{obj_key}' from '{bucket}'")
        return "Sample context text loaded from S3 (simulated)."

    try:
        import boto3
        s3 = boto3.client("s3")
        obj = s3.get_object(Bucket=bucket, Key=obj_key)
        text = obj["Body"].read().decode("utf-8")
        log_info("Context fetched from S3.")
        return text
    except Exception as e:
        log_error(f"Real S3 fetch failed: {e}; falling back to simulated context.")
        return "Sample context text loaded from S3 (simulated)."
