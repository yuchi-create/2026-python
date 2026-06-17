"""
UVA 11417 - GCD（AI 教學簡單版本）

題意：
  給定 N，計算所有 1 <= i < j <= N 的 gcd(i, j) 總和。
  輸入以 N = 0 結束。

解法概念：
  直接用雙重迴圈枚舉所有 (i, j) 配對，呼叫 math.gcd 計算最大公因數並累加。
  N 最大為 500，雙重迴圈最多約 12 萬多次，速度足夠快。
"""

import sys
from math import gcd


def sum_of_gcd(n):
    """計算 1 <= i < j <= n 所有配對的 gcd 總和"""
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total


def main():
    results = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        results.append(str(sum_of_gcd(n)))

    print("\n".join(results))


if __name__ == "__main__":
    main()
