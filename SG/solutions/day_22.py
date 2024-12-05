from pathlib import Path
from collections import defaultdict


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_22_input.txt"

    with open(input_file, "r") as f:
        data = [
            [int(c) for c in b.replace("~", ",").split(",")]
            for b in f.read().split("\n")
        ]
        data.sort(key=lambda l: l[2])

    def fall(inp, skip=None):
        tracker = defaultdict(int)
        fallen = 0

        for ix, (u, v, w, x, y, z) in enumerate(inp):
            if skip == ix:
                continue

            area = [(a, b) for b in range(v, y + 1) for a in range(u, x + 1)]

            highest = max(tracker[a] for a in area) + 1
            for a in area:
                tracker[a] = highest + z - w

            fallen += highest < w
            inp[ix] = (u, v, highest, x, y, highest + z - w)

        return not fallen, fallen

    fall(data)

    res = 0
    for i in range(len(data)):
        res += fall(data.copy(), i)[not p1]

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
