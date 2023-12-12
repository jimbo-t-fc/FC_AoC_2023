from pathlib import Path
from functools import lru_cache


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_12_input.txt"

    with open(input_file, "r") as f:
        data = f.read().split("\n")

    @lru_cache
    def count_ways(lh, lr):
        if not lh:
            return 1 if not lr else 0
        if not lr:
            return 1 if not any("#" in h for h in lh) else 0
        if len(lh[0]) < lr[0]:
            return count_ways(lh[1:], lr) if not "#" in lh[0] else 0
        if lh[0] == "":
            return count_ways(lh[1:], lr)
        if lh[0][0] == "#":
            if len(lh[0]) == lr[0]:
                return count_ways(lh[1:], lr[1:])
            if lh[0][lr[0]] == "#":
                return 0
            ln = lh[0][lr[0] + 1 :], *lh[1:]
            return count_ways(ln, lr[1:])
        if lh[0][0] == "?":
            ln1 = lh[0].replace("?", "#", 1), *lh[1:]
            ln2 = lh[0].replace("?", "", 1), *lh[1:]
            return count_ways(ln1, lr) + count_ways(ln2, lr)

    res = 0
    for d in data:
        hs, r = d.split()
        if not p1:
            hs = ((hs + "?") * 5)[:-1]
            r = ((r + ",") * 5)[:-1]
        hs = tuple(h for h in hs.split(".") if h != "")
        r = tuple(map(int, r.split(",")))
        res += count_ways(hs, r)

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    res2 = solution(input_dir, output_dir, False)
    print("Part 1:", res1)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
