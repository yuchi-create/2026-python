"""
UVA 11349 - Symmetric Matrix（AI 教學簡單版本）

題意：
  給一個 n x n 的矩陣，判斷是否符合以下兩個條件：
    1. 矩陣所有元素都是非負數 (>= 0)
    2. 矩陣關於中心點對稱，也就是 M[i][j] == M[n-1-i][n-1-j]
       （0-indexed 寫法，等價於題目中的 1-indexed M[i][j] = M[n+1-i][n+1-j]）

解法概念：
  把矩陣讀進一個二維 list，逐一檢查每個元素是否 >= 0，
  再檢查 M[i][j] 是否等於「鏡射到中心點」的另一個元素 M[n-1-i][n-1-j]。
  只要其中一個條件不滿足，整個矩陣就是 Non-symmetric。
"""

import sys


def is_symmetric(matrix, n):
    """判斷矩陣是否為「非負且中心對稱」的對稱矩陣"""
    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            # 條件 1：所有元素必須是非負數
            if value < 0:
                return False
            # 條件 2：中心對稱，i,j 對應到 n-1-i, n-1-j
            if value != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1

    results = []
    for case in range(1, t + 1):
        # 下一個 token 會是 "N"，再下一個是 "="，再下一個才是數字
        # 例如輸入格式為：N = 3
        idx += 2  # 跳過 "N" 和 "="
        n = int(data[idx]); idx += 1

        matrix = []
        for _ in range(n):
            row = [int(data[idx + k]) for k in range(n)]
            idx += n
            matrix.append(row)

        if is_symmetric(matrix, n):
            results.append(f"Test #{case}: Symmetric.")
        else:
            results.append(f"Test #{case}: Non-symmetric.")

    print("\n".join(results))


if __name__ == "__main__":
    main()
