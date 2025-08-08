from src.s3_client import fetch_context

def test_fetch_context_simulated_returns_string():
    context = fetch_context()
    assert isinstance(context, str)
    assert len(context) > 0
    assert "simulated" in context.lower()
