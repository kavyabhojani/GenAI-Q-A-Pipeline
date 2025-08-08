import src.bedrock_client as bc

def test_bedrock_fallback_when_pipeline_unavailable(monkeypatch):
    #force the QA pipeline to be unavailable
    monkeypatch.setattr(bc, "qa_pipeline", None, raising=False)

    query = "What is the capital of Canada?"
    context = "Ottawa is the capital city of Canada."

    response = bc.get_response_from_model(query, context)

    assert isinstance(response, str)
    assert response.startswith("[Fallback]"), "Expected fallback response when pipeline is None"
    assert "Unable to run inference" in response
