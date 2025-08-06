import time
from src.validator import check_latency

def dummy_function():
    time.sleep(0.5)
    return "done"

def test_latency_within_limit():
    _, elapsed, within_limit = check_latency(dummy_function, max_latency=2)
    assert within_limit, f"Function exceeded latency limit: {elapsed}s"
