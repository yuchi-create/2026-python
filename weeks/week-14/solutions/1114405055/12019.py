# UVA 12019 - Doom's Day Algorithm（手打版本）
import sys

DOOMSDAY = {1: 10, 2: 21, 3: 7, 4: 4, 5: 9, 6: 6,
            7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]


def main():
    data = sys.stdin.read().split()
    pos = 0
    t = int(data[pos]); pos += 1

    out = []
    for _ in range(t):
        m = int(data[pos]); pos += 1
        d = int(data[pos]); pos += 1
        diff = d - DOOMSDAY[m]
        out.append(WEEKDAYS[(2 + diff) % 7])

    print("\n".join(out))


if __name__ == "__main__":
    main()
