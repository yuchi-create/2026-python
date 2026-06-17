"""
Task 3: Plot timing comparison

This script reads timing results and generates a bar chart.

Recommended workflow:
1. Run Task 1:
   python task1_csv_to_json.py

2. Run Task 2:
   python task2_json_to_xml.py

3. Copy the four [timeit] lines into TIMING_REPORT.md.

4. Run Task 3:
   python task3_plot_comparison.py

Output:
    output/timing_comparison.png
"""

from __future__ import annotations

import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TIMING_REPORT_PATH = BASE_DIR / "TIMING_REPORT.md"
OUTPUT_PATH = BASE_DIR / "output" / "timing_comparison.png"

EXPECTED_FUNCTIONS = [
    "read_csv",
    "write_json",
    "read_json",
    "write_xml",
]


def get_timing_data(report_path: str | Path = TIMING_REPORT_PATH) -> dict[str, float]:
    """
    Read timing data from TIMING_REPORT.md.

    Expected line format:
        [timeit] read_csv 耗時 0.002341s

    If TIMING_REPORT.md does not exist or does not contain timing data,
    this function returns demo values so the chart can still be generated.
    Remember to replace demo values with your real runtime results before submission.
    """
    report_path = Path(report_path)
    timing_data: dict[str, float] = {}

    if report_path.exists():
        content = report_path.read_text(encoding="utf-8")

        pattern = re.compile(
            r"\[timeit\]\s+(\w+)\s+耗時\s+([0-9]*\.?[0-9]+)s"
        )

        for function_name, seconds in pattern.findall(content):
            if function_name in EXPECTED_FUNCTIONS:
                timing_data[function_name] = float(seconds)

    if not timing_data:
        # Demo fallback values.
        # Replace these by writing your actual timeit results into TIMING_REPORT.md.
        timing_data = {
            "read_csv": 0.002341,
            "write_json": 0.001203,
            "read_json": 0.000891,
            "write_xml": 0.003412,
        }

    # Keep the chart order stable.
    return {
        function_name: timing_data.get(function_name, 0.0)
        for function_name in EXPECTED_FUNCTIONS
    }


def plot_timing_comparison(
    timing_data: dict[str, float],
    output_path: str | Path = OUTPUT_PATH,
) -> None:
    """
    Draw a bar chart and save it to output/timing_comparison.png.

    Requirements:
    - Bar chart
    - English title and axis labels
    - Runtime number shown on each bar
    - Create output directory automatically
    """
    import matplotlib.pyplot as plt

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    function_names = list(timing_data.keys())
    runtimes = list(timing_data.values())

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(function_names, runtimes)

    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")

    max_runtime = max(runtimes) if runtimes else 0
    y_margin = max_runtime * 0.15 if max_runtime > 0 else 0.001
    ax.set_ylim(0, max_runtime + y_margin)

    for bar, runtime in zip(bars, runtimes):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{runtime:.6f}s",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def main() -> None:
    timing_data = get_timing_data()
    plot_timing_comparison(timing_data, OUTPUT_PATH)
    print(f"圖表已儲存：{OUTPUT_PATH.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
