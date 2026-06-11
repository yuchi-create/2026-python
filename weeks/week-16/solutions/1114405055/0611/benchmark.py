"""Stage 2 — 排序效能量測

執行：python benchmark.py
輸出：比較表（stdout）+ results.json
"""

import json
import random

from sorts import bubble_sort, merge_sort, quick_sort
from timing import timeit


def make_data(n: int, seed: int = 42) -> list:
    """產生固定亂數序列，seed 固定以確保實驗可重現"""
    rng = random.Random(seed)
    return [rng.randint(0, n * 10) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    """對各排序演算法量測平均耗時，回傳 {algo_name: {str(n): avg_sec}}"""
    algos = {
        "bubble_sort": timeit(bubble_sort),
        "quick_sort": timeit(quick_sort),
        "merge_sort": timeit(merge_sort),
        "timsort_builtin": timeit(sorted),
    }
    results: dict = {name: {} for name in algos}

    for n in sizes:
        for name, fn in algos.items():
            times = []
            for _ in range(repeats):
                data = make_data(n)
                fn(data)
                times.append(fn.last_elapsed)
            results[name][str(n)] = sum(times) / len(times)

    return results


def _print_table(results: dict) -> None:
    algos = list(results.keys())
    sizes = list(next(iter(results.values())).keys())
    col = 18
    header = f"{'n':>6}" + "".join(f"{a:>{col}}" for a in algos)
    print(header)
    print("-" * len(header))
    for n in sizes:
        row = f"{n:>6}" + "".join(f"{results[a][n]:>{col}.6f}" for a in algos)
        print(row)


if __name__ == "__main__":
    print("正在執行 benchmark，請稍候…")
    results = run_benchmark()
    _print_table(results)

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print("\nresults.json 已儲存")
