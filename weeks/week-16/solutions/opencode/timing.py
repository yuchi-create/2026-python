import functools
import time


def timeit(func):
    """記錄被裝飾函式每次呼叫的耗時"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        wrapper.records.append(elapsed)
        wrapper.last_elapsed = elapsed
        return result

    wrapper.records = []
    wrapper.last_elapsed = None
    return wrapper
