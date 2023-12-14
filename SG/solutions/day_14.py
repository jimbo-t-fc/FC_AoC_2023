from pathlib import Path
from tqdm import tqdm
from collections import defaultdict


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_14_input.txt"

    rocks = {"O": [], "#": {0: defaultdict(list), 1: defaultdict(list)}}
    with open(input_file, "r") as f:
        for ROW, row in enumerate(f.read().split("\n")):
            for COL, rock in enumerate(row):
                if rock == "O":
                    rocks[rock].append([ROW, COL])
                if rock == "#":
                    rocks[rock][0][ROW].append(COL)
                    rocks[rock][1][COL].append(ROW)

    def rotate(direction):
        ns, se = direction in "NS", direction in "SE"
        mult = 1 - 2 * se

        rocks["O"].sort(key=lambda r: r[ns])
        cur = free = default = ROW * se
        for rock in rocks["O"][::mult]:
            if cur != rock[ns]:
                free = default
                cur = rock[ns]

            cubes = (
                r + mult
                for r in rocks["#"][ns][cur]
                if (mult * (r - rock[not ns]) < 0)
            )
            rock[not ns] = (
                min(free, *cubes, default) if se else max(free, *cubes, default)
            )
            free = rock[not ns] + mult

    cycles = {}
    cycle = 0
    jumped = False
    nc = 1 if p1 else 1000000000

    while cycle < nc:
        cycle += 1

        for d in "N" if p1 else "NWSE":
            rotate(d)

        s = "".join(["".join(str(r)) for r in rocks["O"]])
        if not jumped and s in cycles:
            cycle += (cycle - cycles[s]) * ((nc - cycle) // (cycle - cycles[s]))
            jumped = True
        else:
            cycles[s] = cycle

    res = sum(ROW + 1 - r[0] for r in rocks["O"])

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
