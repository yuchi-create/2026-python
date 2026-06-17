"""
R02：例外處理基本用法（註解版參考程式）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

執行：
    python R02-exceptions-basic.py
"""
import traceback


# ---------- 14.6 多個例外 ----------
def parse_value(s):
    """同一個 except 用 tuple 列出多種例外類別，共用同一段處理邏輯。"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # ValueError：字串內容無法轉成整數（例如 "abc"）。
        # TypeError ：傳入的根本不是字串／數字（例如 None）。
        # 兩種情況的處理方式相同，所以合併在同一個 except。
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """except Exception，而不是裸 except:（裸 except 連 KeyboardInterrupt、SystemExit 都會抓到，容易讓程式無法正常中斷）"""
    try:
        return func(*args)
    except Exception as e:
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # traceback.print_exc() 印出完整呼叫堆疊，方便除錯，
        # 比只印 str(e) 能看到問題發生的確切位置。
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException，
    這樣外部程式碼可以用一個 except NetworkError 統一接住所有子類別。"""


class HostnameError(NetworkError):
    """找不到主機；不需要額外屬性，直接沿用 Exception 的訊息機制即可。"""


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層程式碼判斷是哪台主機、等了多久。"""
    def __init__(self, host, seconds):
        # 先呼叫 super().__init__ 設定好例外訊息，
        # 再額外保存 host / seconds，讓 except 區塊可以直接讀取這些資訊。
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- 14.6 ---")
    parse_value("abc")
    parse_value(None)

    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)

    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            # 因為 HostnameError / ConnectionTimeout 都繼承自 NetworkError，
            # 這一個 except 就能同時接住兩種子類別的例外。
            print(f"接到 {type(e).__name__}: {e}")
