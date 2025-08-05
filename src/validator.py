import time

def check_latency(function, *args, max_latency=2, **kwargs):
    """
    Measures the time taken by a function and compares it against max_latency.
    Returns a tuple (result, elapsed_time, is_within_limit).
    """
    start_time = time.time()
    result = function(*args, **kwargs)
    elapsed = time.time() - start_time
    is_within_limit = elapsed <= max_latency
    return result, elapsed, is_within_limit
