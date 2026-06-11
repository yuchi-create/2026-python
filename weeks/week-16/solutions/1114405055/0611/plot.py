"""Stage 4 — 讀取 results.json，畫折線圖（y 軸 log scale）"""

import json
import os

import matplotlib
matplotlib.use("Agg")  # 無視窗環境必要
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """讀取 results.json，回傳 dict。使用 json 而非 pickle（CWE-502）"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    """畫折線圖並儲存為 PNG。

    x 軸：資料量 n
    y 軸：平均秒數（log scale）
    每個演算法一條線。
    """
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    markers = ["o", "s", "^", "D", "v"]
    for idx, (name, data) in enumerate(results.items()):
        sizes = [int(n) for n in data.keys()]
        times = list(data.values())
        ax.plot(sizes, times, marker=markers[idx % len(markers)], label=name)

    ax.set_xlabel("Data Size n")
    ax.set_ylabel("Average Time (s, log scale)")
    ax.set_yscale("log")
    ax.set_title("Sorting Algorithm Performance")
    ax.legend()
    ax.grid(True, which="both", linestyle="--", alpha=0.5)

    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    results = load_results("results.json")
    plot_results(results, "assets/benchmark.png")
    print("assets/benchmark.png 已儲存")
