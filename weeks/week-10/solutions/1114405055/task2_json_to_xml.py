"""
Task 2: JSON to XML

Responsibilities:
1. Read Task 1 JSON output.
2. Convert student list into XML.
3. Export result to XML.
4. Measure read_json and write_xml runtime with @timeit.
"""

from __future__ import annotations

import json
import os
import time
import xml.etree.ElementTree as ET
from functools import wraps


DEFAULT_JSON_PATH = "output/students.json"
DEFAULT_XML_PATH = "output/students.xml"


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
def read_json(filepath: str) -> dict:
    """
    Read JSON file.
    """
    with open(filepath, mode="r", encoding="utf-8") as json_file:
        return json.load(json_file)


def build_xml_tree(data: dict) -> ET.Element:
    """
    Convert JSON data into XML ElementTree root.

    Expected root:
        <students source="113年新生資料庫" total="2">

    Expected student:
        <student id="1130001" dept="資訊工程系" school="國立馬公高中" zip="880" />
    """
    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(data.get("總人數", 0)),
        },
    )

    students = data.get("學生清單", [])

    for student in students:
        ET.SubElement(
            root,
            "student",
            {
                "id": str(student.get("學號", "")),
                "dept": str(student.get("系所名稱", "")),
                "school": str(student.get("畢業學校", "")),
                "zip": str(student.get("郵遞區號", "")),
            },
        )

    return root


@timeit
def write_xml(data: dict, filepath: str) -> None:
    """
    Write XML to file.

    Requirements:
    - XML declaration
    - UTF-8 encoding
    - create output directory if needed
    """
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)

    root = build_xml_tree(data)
    tree = ET.ElementTree(root)

    try:
        ET.indent(tree, space="  ", level=0)
    except AttributeError:
        # ET.indent is available in Python 3.9+.
        pass

    tree.write(filepath, encoding="utf-8", xml_declaration=True)


def main() -> None:
    """
    Suggested flow:
    1. Read output/students.json.
    2. Convert data to XML.
    3. Write output/students.xml.
    """
    data = read_json(DEFAULT_JSON_PATH)
    write_xml(data, DEFAULT_XML_PATH)

    print(f"XML 已儲存：{DEFAULT_XML_PATH}")


if __name__ == "__main__":
    main()
