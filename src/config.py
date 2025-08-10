#config constants for GenAI Q&A Pipeline.

#toggle simulated vs real S3 (real path to be wired with boto3 later)
USE_REAL_S3 = False

S3_BUCKET_NAME = "genai-qa-pipeline-context"
CONTEXT_FILE_KEY = "context.txt"

#placeholder
DEFAULT_MODEL = "bedrock.simulated.huggingface"

DEFAULT_MAX_LATENCY = 2.0
