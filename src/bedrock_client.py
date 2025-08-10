from src.logger import log_info, log_error

_qa_pipeline = None  #lazy init

def _lazy_init_pipeline():
    global _qa_pipeline
    if _qa_pipeline is not None:
        return
    try:
        from transformers import pipeline
        _qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
        log_info("Hugging Face QA pipeline initialized.")
    except Exception as e:
        _qa_pipeline = None
        log_error(f"Failed to initialize Hugging Face pipeline: {e}")

def get_response_from_model(query: str, context: str) -> str:
    _lazy_init_pipeline()

    if not context or len(context.strip()) < 10:
        return "Insufficient context provided to generate a reliable answer."

    if _qa_pipeline is None:
        log_error("QA pipeline not available. Returning fallback response.")
        return f"[Fallback] Unable to run inference. Query: {query[:60]}..."

    result = _qa_pipeline(question=query, context=context)
    answer = (result.get("answer") or "").strip()
    return answer or "[No answer generated]"
