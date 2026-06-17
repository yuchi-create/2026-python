# UVA 11349 - Symmetric Matrix（手打版本）
import sys


def main():
    data = sys.stdin.read().split()
    pos = 0
    t = int(data[pos]); pos += 1

    out = []
    for case in range(1, t + 1):
        pos += 2  # 跳過 "N" "="
        n = int(data[pos]); pos += 1

        mat = []
        for i in range(n):
            row = list(map(int, data[pos:pos + n]))
            pos += n
            mat.append(row)

        ok = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] < 0 or mat[i][j] != mat[n - 1 - i][n - 1 - j]:
                    ok = False
                    break
            if not ok:
                break

        if ok:
            out.append(f"Test #{case}: Symmetric.")
        else:
            out.append(f"Test #{case}: Non-symmetric.")

    print("\n".join(out))


if __name__ == "__main__":
    main()
