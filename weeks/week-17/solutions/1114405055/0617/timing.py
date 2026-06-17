"""0617 任務一 — timeit 計時裝飾器

timeit(repeat=3) 回傳一個裝飾器:
  - 被裝飾函式的回傳值不變
  - 每次呼叫實際跑 repeat 次,每次耗時(秒)append 到 wrapper.records
  - wrapper.last_elapsed = 本次 repeat 的平均耗時
  - 裝飾器內不 print
  - repeat 必須是 int 且 >= 1,否則 raise ValueError(不用 assert)
  - 被裝飾函式拋出例外時原樣往外傳,該輪不計入 records
"""

import functools
import time


def timeit(repeat=3):
    if not isinstance(repeat, int) or isinstance(repeat, bool) or repeat < 1:
        raise ValueError(f"repeat must be an int >= 1, got {repeat!r}")

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            elapsed_times = []
            result = None
            for _ in range(repeat):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                elapsed = time.perf_counter() - start
                elapsed_times.append(elapsed)
                wrapper.records.append(elapsed)
            wrapper.last_elapsed = sum(elapsed_times) / len(elapsed_times)
            return result

        wrapper.records = []
        wrapper.last_elapsed = None
        return wrapper

    return decorator
