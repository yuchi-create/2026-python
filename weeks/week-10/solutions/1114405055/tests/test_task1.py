import unittest

from task1_csv_to_json import filter_by_admission, count_by_dept


class TestTask1CsvToJson(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {
                "學號": "1130001",
                "系所名稱": "資訊工程系",
                "入學方式": "聯合登記分發",
                "畢業學校": "國立馬公高中",
                "郵遞區號": "880",
            },
            {
                "學號": "1130002",
                "系所名稱": "電機工程系",
                "入學方式": "個人申請",
                "畢業學校": "國立澎湖高中",
                "郵遞區號": "880",
            },
            {
                "學號": "1130003",
                "系所名稱": "資訊工程系",
                "入學方式": "聯合登記分發",
                "畢業學校": "國立馬公高中",
                "郵遞區號": "880",
            },
            {
                "學號": "1130004",
                "系所名稱": "食品科學系",
                "入學方式": "聯合登記分發",
                "畢業學校": "國立澎湖高中",
                "郵遞區號": "880",
            },
        ]

    def test_filter_keeps_correct_rows(self):
        result = filter_by_admission(self.rows, "聯合登記分發")

        self.assertEqual(len(result), 3)
        for row in result:
            self.assertEqual(row["入學方式"], "聯合登記分發")

    def test_filter_removes_others(self):
        result = filter_by_admission(self.rows, "聯合登記分發")

        admission_methods = [row["入學方式"] for row in result]
        self.assertNotIn("個人申請", admission_methods)

    def test_filter_empty_input(self):
        result = filter_by_admission([], "聯合登記分發")

        self.assertEqual(result, [])

    def test_filter_missing_admission_key(self):
        rows = [
            {"學號": "1130001", "系所名稱": "資訊工程系"},
            {"學號": "1130002", "系所名稱": "電機工程系", "入學方式": "聯合登記分發"},
        ]

        result = filter_by_admission(rows, "聯合登記分發")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["學號"], "1130002")

    def test_count_by_dept_correct(self):
        filtered_rows = filter_by_admission(self.rows, "聯合登記分發")

        result = count_by_dept(filtered_rows)

        expected = {
            "資訊工程系": 2,
            "食品科學系": 1,
        }
        self.assertEqual(result, expected)

    def test_count_by_dept_empty(self):
        result = count_by_dept([])

        self.assertEqual(result, {})

    def test_count_by_dept_missing_dept_name(self):
        rows = [
            {"學號": "1130001", "系所名稱": "資訊工程系"},
            {"學號": "1130002"},
            {"學號": "1130003", "系所名稱": "資訊工程系"},
        ]

        result = count_by_dept(rows)

        self.assertEqual(result, {"資訊工程系": 2})


if __name__ == "__main__":
    unittest.main()
