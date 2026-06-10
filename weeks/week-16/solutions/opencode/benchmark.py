import json
import random

from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import bubble_sort_fast, quick_sort_fast


def make_data(n: int, seed: int = 42) -> list:
    random.seed(seed)
    return [random.randint(-10000, 10000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    funcs = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "bubble_sort_fast": bubble_sort_fast,
        "quick_sort_fast": quick_sort_fast,
    }

    results = {}
    for name, func in funcs.items():
        timed_func = timeit(func)
        results[name] = {}
        for n in sizes:
            timed_func.records = []
            data = make_data(n)
            for _ in range(repeats):
                timed_func(data)
            mean = sum(timed_func.records) / len(timed_func.records)
            results[name][str(n)] = {
                "mean": round(mean, 8),
                "records": [round(r, 8) for r in timed_func.records],
            }

    return results


if __name__ == "__main__":
    sizes = (500, 1000, 2000, 4000)
    results = run_benchmark(sizes=sizes, repeats=3)

    header = f"{'演算法':>20}" + "".join(f"{n:>12}" for n in sizes)
    print(header)
    print("-" * len(header))
    for name, data in results.items():
        row = f"{name:>20}"
        for n in sizes:
            row += f"{data[str(n)]['mean']:>12.6f}"
        print(row)

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("\nresults.json 已儲存")
