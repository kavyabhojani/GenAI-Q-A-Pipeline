from src.model_interface import pipeline_status

def test_pipeline_status_returns_string():
    status = pipeline_status()
    assert isinstance(status, str)
    assert status in {"Ready", "Not Initialized"}
