"""Stage 1 — @timeit 計時裝飾器"""

import functools
import time


def timeit(func):
    """量測被裝飾函式每次呼叫的執行時間。

    屬性（掛在 wrapper 上）：
        last_elapsed: float  — 最近一次耗時（秒）
        records: list[float] — 歷次耗時列表（累積）

    不含任何 print；格式化輸出由呼叫方（benchmark）負責。
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        wrapper.last_elapsed = elapsed
        wrapper.records.append(elapsed)
        return result

    wrapper.last_elapsed = None
    wrapper.records = []
    return wrapper
