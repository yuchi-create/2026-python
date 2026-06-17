# UVA 11417 - GCD（手打版本）
import sys
from math import gcd


def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break

        total = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += gcd(i, j)
        out.append(str(total))

    print("\n".join(out))


if __name__ == "__main__":
    main()
