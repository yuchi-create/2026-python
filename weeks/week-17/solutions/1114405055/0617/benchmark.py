"""0617 任務二 — 用 timing.timeit 量 linear_search 與 binary_search

跑法:python benchmark.py
"""

from timing import timeit
from search import linear_search, binary_search

N = 200_000
data = list(range(N))
target = N - 1  # 刻意挑最壞情況(linear 要找到最後一個)


@timeit(repeat=5)
def run_linear():
    return linear_search(data, target)


@timeit(repeat=5)
def run_binary():
    return binary_search(data, target)


if __name__ == "__main__":
    run_linear()
    run_binary()

    print(f"n = {N}, target = 最後一個元素(最壞情況)")
    print(f"linear_search  records = {run_linear.records}")
    print(f"linear_search  last_elapsed (avg of {len(run_linear.records)} runs) = {run_linear.last_elapsed:.6f} s")
    print(f"binary_search  records = {run_binary.records}")
    print(f"binary_search  last_elapsed (avg of {len(run_binary.records)} runs) = {run_binary.last_elapsed:.6f} s")
    ratio = run_linear.last_elapsed / run_binary.last_elapsed
    print(f"linear / binary 倍數 = {ratio:.1f}x")
