# UVA 11461 - Square Numbers（手打版本）
import sys
from math import isqrt


def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        out.append(str(isqrt(b) - isqrt(a - 1)))

    print("\n".join(out))


if __name__ == "__main__":
    main()
