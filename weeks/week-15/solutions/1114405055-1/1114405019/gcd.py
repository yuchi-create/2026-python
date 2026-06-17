from math import gcd


def sum_of_gcd(n: int) -> int:
    if n < 2:
        return 0
    return sum(gcd(a, b) for a in range(1, n) for b in range(a + 1, n + 1))
