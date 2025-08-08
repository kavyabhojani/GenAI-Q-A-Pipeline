from transformers import pipeline
from src.logger import log_info, log_error

#initializing hugging face QA pipeline
try:
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    log_info("Hugging Face QA pipeline initialized.")
except Exception as e:
    qa_pipeline = None
    log_error(f"Failed to initialize Hugging Face pipeline: {e}")

def get_response_from_model(query: str, context: str) -> str:
    """
    Generate a response using the QA pipeline (simulated Bedrock).
    Falls back to a static message if the pipeline is unavailable.
    """
    if qa_pipeline is None:
        log_error("QA pipeline not available. Returning fallback response.")
        return f"[Fallback] Unable to run inference. Query: {query[:60]}..."

    log_info(f"Running inference for query (context length: {len(context)})...")
    #minimal guardrails so empty or short context doesn't blow up
    if not context or len(context.strip()) < 10:
        return "Insufficient context provided to generate a reliable answer."

    result = qa_pipeline(question=query, context=context)
    answer = result.get("answer", "").strip() or "[No answer generated]"
    return answer
