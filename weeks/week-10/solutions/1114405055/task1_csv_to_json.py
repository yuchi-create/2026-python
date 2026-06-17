"""
Task 1: CSV to JSON

Responsibilities:
1. Read CSV with UTF-8-BOM encoding.
2. Filter students by admission method.
3. Count students by department.
4. Export result to JSON.
5. Measure read_csv and write_json runtime with @timeit.
"""

from __future__ import annotations

import csv
import json
import os
import time
from functools import wraps


DEFAULT_CSV_PATH = "../../../../assets/stu-data/113年新生資料庫.csv"
DEFAULT_OUTPUT_PATH = "output/students.json"
TARGET_ADMISSION_METHOD = "聯合登記分發"


def timeit(func):
    """
    Measure function execution time and print:
    [timeit] function_name 耗時 0.000000s
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


@timeit
def read_csv(filepath: str) -> list[dict]:
    """
    Read CSV file with UTF-8-BOM encoding.

    Args:
        filepath: CSV file path.

    Returns:
        A list of row dictionaries.
    """
    rows: list[dict] = []

    with open(filepath, mode="r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(dict(row))

    return rows


@timeit
def write_json(data: dict, filepath: str) -> None:
    """
    Write dict data to JSON file.

    Requirements:
    - ensure_ascii=False
    - indent=2
    - create output directory if needed
    """
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filepath, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    """
    Keep only rows where 入學方式 == method.

    Missing 入學方式 should be ignored.
    """
    return [
        row
        for row in rows
        if row.get("入學方式") == method
    ]


def count_by_dept(rows: list[dict]) -> dict:
    """
    Count students by 系所名稱.

    Missing 系所名稱 should be ignored.
    """
    dept_count: dict[str, int] = {}

    for row in rows:
        dept = row.get("系所名稱")

        if not dept:
            continue

        dept_count[dept] = dept_count.get(dept, 0) + 1

    return dept_count


def build_output_data(filtered_rows: list[dict], dept_count: dict) -> dict:
    """
    Build final JSON structure.
    """
    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": TARGET_ADMISSION_METHOD,
        "總人數": len(filtered_rows),
        "系所統計": dept_count,
        "學生清單": filtered_rows,
    }


def main() -> None:
    """
    Suggested flow:
    1. Read source CSV.
    2. Filter 入學方式 == 聯合登記分發.
    3. Count by department.
    4. Build output data.
    5. Write output/students.json.
    """
    rows = read_csv(DEFAULT_CSV_PATH)
    filtered_rows = filter_by_admission(rows, TARGET_ADMISSION_METHOD)
    dept_count = count_by_dept(filtered_rows)
    output_data = build_output_data(filtered_rows, dept_count)
    write_json(output_data, DEFAULT_OUTPUT_PATH)

    print(f"JSON 已儲存：{DEFAULT_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
