import time
from typing import Any, Callable, Tuple
from src.logger import log_info

def check_latency(function: Callable[..., Any], *args, max_latency: float = 2.0, **kwargs) -> Tuple[Any, float, bool]:

    log_info(f"Validating latency (limit={max_latency}s)...")
    start = time.time()
    result = function(*args, **kwargs)
    elapsed = time.time() - start
    within_limit = elapsed <= max_latency
    log_info(f"Latency measured: {elapsed:.4f}s (within limit: {within_limit})")
    return result, elapsed, within_limit
