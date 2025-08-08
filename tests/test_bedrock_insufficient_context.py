import src.bedrock_client as bc

def test_insufficient_context_returns_safe_message(monkeypatch):

    if getattr(bc, "qa_pipeline", None) is None:
        import pytest
        pytest.skip("HF pipeline not available; insufficient-context path requires pipeline")

    query = "Explain cloud computing in one line."
    context = "  "  # empty/whitespace -> insufficient

    response = bc.get_response_from_model(query, context)

    assert isinstance(response, str)
    assert "Insufficient context" in response
