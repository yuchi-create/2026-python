"""
R03：效能測量基本用法（註解版參考程式）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

執行：
    python R03-profile-basic.py
"""
import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


# ---------- 計時裝飾器（粗粒度） ----------
def timed(func):
    # @wraps(func) 保留原函式的 __name__ / __doc__ 等資訊，
    # 否則被裝飾後 func.__name__ 會變成 "wrapper"，不利除錯與內省。
    @wraps(func)
    def wrapper(*args, **kwargs):
        # time.perf_counter() 是高精度計時器，適合用來量「相對時間長度」，
        # 不適合拿來當作絕對時間（牆上時鐘）使用。
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    # timeit 會把同一段程式碼重複執行 number 次再取總時間，
    # 這樣可以避免單次測量受系統雜訊（如排程、快取）影響太大。
    n = 10_000
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    # cProfile 會記錄程式執行期間，每個函式被呼叫的次數與耗時，
    # 適合用來找出「整支程式裡真正拖慢效能的部分」，
    # 而不是像 timeit 只能量一小段程式碼。
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    # sort_stats("cumulative") 依累積耗時排序（包含呼叫的子函式），
    # print_stats(5) 只列出前 5 名，避免輸出過長。
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
