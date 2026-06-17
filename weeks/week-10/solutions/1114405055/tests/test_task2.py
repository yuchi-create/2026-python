import unittest
import xml.etree.ElementTree as ET

from task2_json_to_xml import build_xml_tree


class TestTask2JsonToXml(unittest.TestCase):
    def setUp(self):
        self.data = {
            "來源": "113年新生資料庫",
            "入學方式篩選": "聯合登記分發",
            "總人數": 2,
            "系所統計": {
                "資訊工程系": 1,
                "電機工程系": 1,
            },
            "學生清單": [
                {
                    "學號": "1130001",
                    "系所名稱": "資訊工程系",
                    "畢業學校": "國立馬公高中",
                    "郵遞區號": "880",
                },
                {
                    "學號": "1130002",
                    "系所名稱": "電機工程系",
                    "畢業學校": "國立澎湖高中",
                    "郵遞區號": "880",
                },
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.data)

        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["source"], "113年新生資料庫")
        self.assertEqual(root.attrib["total"], "2")

    def test_student_count_matches(self):
        root = build_xml_tree(self.data)
        students = root.findall("student")

        self.assertEqual(len(students), 2)

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.data)
        student = root.findall("student")[0]

        self.assertIn("id", student.attrib)
        self.assertIn("dept", student.attrib)
        self.assertIn("school", student.attrib)
        self.assertIn("zip", student.attrib)

    def test_student_attrs_values_correct(self):
        root = build_xml_tree(self.data)
        student = root.findall("student")[0]

        self.assertEqual(student.attrib["id"], "1130001")
        self.assertEqual(student.attrib["dept"], "資訊工程系")
        self.assertEqual(student.attrib["school"], "國立馬公高中")
        self.assertEqual(student.attrib["zip"], "880")

    def test_empty_student_list(self):
        data = {
            "來源": "113年新生資料庫",
            "入學方式篩選": "聯合登記分發",
            "總人數": 0,
            "系所統計": {},
            "學生清單": [],
        }

        root = build_xml_tree(data)
        students = root.findall("student")

        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["total"], "0")
        self.assertEqual(len(students), 0)

    def test_xml_is_valid(self):
        root = build_xml_tree(self.data)
        xml_string = ET.tostring(root, encoding="unicode")

        parsed_root = ET.fromstring(xml_string)

        self.assertEqual(parsed_root.tag, "students")

    def test_missing_student_fields_use_empty_string(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 1,
            "學生清單": [
                {
                    "學號": "1130001",
                }
            ],
        }

        root = build_xml_tree(data)
        student = root.find("student")

        self.assertEqual(student.attrib["id"], "1130001")
        self.assertEqual(student.attrib["dept"], "")
        self.assertEqual(student.attrib["school"], "")
        self.assertEqual(student.attrib["zip"], "")


if __name__ == "__main__":
    unittest.main()
