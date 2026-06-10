import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = [
    "Heiti TC", "Microsoft JhengHei", "Noto Sans CJK SC",
]
plt.rcParams["axes.unicode_minus"] = False


def load_results(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    sizes = sorted(int(n) for n in next(iter(results.values())).keys())
    plt.figure(figsize=(10, 6))

    for name, data in results.items():
        means = [data[str(n)]["mean"] for n in sizes]
        plt.plot(sizes, means, marker="o", label=name)

    plt.xlabel("資料量 n")
    plt.ylabel("平均耗時 (秒)")
    plt.yscale("log")
    plt.title("排序演算法效能比較")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
