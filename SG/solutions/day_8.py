from pathlib import Path
import math


def solution(input_dir, output_dir, part):
    input_file = Path(input_dir) / "day_8_input.txt"

    res = None
    with open(input_file, "r") as f:
        ins, maps = f.read().split("\n\n")
        ins = ins.replace("L", "0").replace("R", "1")

        all_maps = {}
        for m in maps.split("\n"):
            s, d = m.split(" = ")
            all_maps[s] = tuple(ds for ds in d[1:-1].split(", "))

    starts = ["AAA"] if part == "p1" else [k for k in all_maps.keys() if k[-1] == "A"]
    steps = []
    for start in starts:
        step = c = 0
        while True:
            step += 1
            dest = all_maps[start][int(ins[c % len(ins)])]
            if dest == "ZZZ" or (part == "p2" and dest[-1] == "Z"):
                break
            start = dest
            c += 1
        steps.append(step)

    return math.lcm(*steps)


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, "p1")
    res2 = solution(input_dir, output_dir, "p2")
    print("Part 1:", res1)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
