"""
UVA 12019 - Doom's Day Algorithm（AI 教學簡單版本）

題意：
  2012 年每個月有一個「Doomsday」日期，且這些日期都落在同一個星期幾（2012 年是星期三）。
  給定月份 m 與日期 d，求這天是星期幾。

解法概念：
  先建立一個表，記錄 2012 年每個月的 Doomsday 日期。
  計算 d 與該月 Doomsday 日期的差距 diff = d - doomsday[m]，
  這個差距除以 7 取餘數，就是與星期三相差的天數，
  再從星期三往前或往後數，就能得到答案。
  Python 的 % 對負數也會回傳非負的餘數，所以不用額外處理負數情況。
"""

import sys

# 2012 年每個月的 Doomsday 日期（1-indexed 月份）
DOOMSDAY = {
    1: 10, 2: 21, 3: 7, 4: 4, 5: 9, 6: 6,
    7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12,
}

# 星期幾的名稱列表，Wednesday 在 index 2
WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday",
]
WEDNESDAY_INDEX = 2


def weekday_of(m, d):
    """回傳 2012 年 m 月 d 日是星期幾"""
    diff = d - DOOMSDAY[m]
    index = (WEDNESDAY_INDEX + diff) % 7
    return WEEKDAYS[index]


def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1

    results = []
    for _ in range(t):
        m = int(data[idx]); idx += 1
        d = int(data[idx]); idx += 1
        results.append(weekday_of(m, d))

    print("\n".join(results))


if __name__ == "__main__":
    main()
