"""
R01：unittest 基本用法（註解版參考程式）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁（mock.patch）
- 14.3 在單元測試中測試例外情況

執行：
    python R01-unittest-basics.py
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------
def url_print(host, domain):
    # 這個函式只會把組好的網址印到 stdout，沒有回傳值，
    # 所以測試時要驗證「印出來的內容」而不是回傳值。
    print(f"https://{host}.{domain}")


def parse_int(s):
    # 故意對空字串拋出明確訊息的 ValueError，方便示範 14.3 的例外測試。
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    # api 是外部依賴（例如 HTTP client），測試時不會真的打 API，
    # 而是用 mock 物件替換，這就是 14.2 的核心情境。
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # io.StringIO() 建立一個「假的檔案物件」，存在記憶體中。
        buf = io.StringIO()
        # redirect_stdout 把 print() 原本要送到終端機的內容，
        # 暫時導向到 buf，這樣才能在測試裡檢查印出的字串。
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # getvalue() 取出緩衝區內容；strip() 去掉結尾的換行符再比較。
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # MagicMock() 會自動產生任何屬性/方法呼叫，不會丟錯，
        # 適合用來模擬一個我們還沒實作、或不想真的呼叫的物件。
        fake_api = MagicMock()
        # 設定 fake_api.get(...) 被呼叫時要回傳什麼。
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        # assert_called_once_with 同時驗證「只被呼叫一次」且「參數正確」，
        # 比單純檢查回傳值更能保證程式邏輯正確。
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # @patch 裝飾器會在測試執行期間，把 builtins.print 換成 mock_print，
        # 測試結束後自動還原，不會影響其他測試。
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # assertRaises 只檢查「有沒有丟出指定類型的例外」，
        # with 區塊內的程式碼一旦丟出 ValueError 就視為通過。
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # assertRaisesRegex 多檢查一層：例外訊息是否符合正規表達式，
        # 確保丟出的不只是「對的類型」，訊息內容也合理。
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 正常路徑也要測，避免只顧著測例外而漏掉基本功能。
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
