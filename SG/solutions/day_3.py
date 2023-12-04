from pathlib import Path
import re
from math import prod
import timeit


def solution(input_dir, output_dir):
    input_file = Path(input_dir) / "day_3_input.txt"
    symbols = {}

    with open(input_file, "r") as f:
        lines = f.readlines()
        # store symbols
        for row, l in enumerate(lines):
            for m in re.finditer(r"[^.\d\s]", l):
                symbols[(row, m.start())] = {"sym": m.group(), "nums": []}

        for row, l in enumerate(lines):
            for m in re.finditer(r"\d+", l):
                # look for symbols around digit
                for r in range(row - 1, row + 2):
                    for c in range(m.start() - 1, m.end() + 1):
                        if (r, c) in symbols:
                            symbols[(r, c)]["nums"].append(int(m.group()))

    sum_parts = sum_gears = 0
    for _, s in symbols.items():
        sum_parts += sum(s["nums"])
        sum_gears += (
            prod(s["nums"]) if (s["sym"] == "*") and (len(s["nums"]) == 2) else 0
        )

    return sum_parts, sum_gears


def main(input_dir="../input", output_dir="../output"):
    res1, res2 = solution(input_dir, output_dir)
    print(res1)
    print(res2)


if __name__ == "__main__":
    # print(timeit.timeit(main, number=1000) / 1000)
    main()
