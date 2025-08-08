"""
End-to-end test for the main GenAI Q&A Pipeline flow
"""

from src.s3_client import fetch_context
from src.model_interface import get_response_from_model
from src.validator import check_latency


def test_end_to_end_flow():
    query = "What is the capital of Canada?"
    context = fetch_context()

    response, latency, within_limit = check_latency(get_response_from_model, query, context)

    assert isinstance(response, str)
    assert len(response) > 0
    assert isinstance(latency, float)
    assert within_limit is True
