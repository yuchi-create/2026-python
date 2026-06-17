"""
UVA 11461 - Square Numbers（AI 教學簡單版本）

題意：
  給定 a, b，求 [a, b] 區間中完全平方數的個數。
  輸入以 a = 0, b = 0 結束。

解法概念：
  完全平方數在 [1, x] 範圍中總共有 floor(sqrt(x)) 個（因為 1^2, 2^2, ..., floor(sqrt(x))^2 都 <= x）。
  所以 [a, b] 中完全平方數個數 = floor(sqrt(b)) - floor(sqrt(a - 1))。
  用 math.isqrt 可以避免浮點數誤差，得到精確的整數平方根。
"""

import sys
from math import isqrt


def count_squares(a, b):
    """計算 [a, b] 區間內完全平方數的個數"""
    return isqrt(b) - isqrt(a - 1)


def main():
    results = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        results.append(str(count_squares(a, b)))

    print("\n".join(results))


if __name__ == "__main__":
    main()
