from pathlib import Path
from math import floor, ceil, sqrt


def solution(input_dir, output_dir, part):
    input_file = Path(input_dir) / "day_6_input.txt"

    res = 1
    with open(input_file, "r") as f:
        if part == "p1":
            tds = zip(*[list(map(int, l.split(":")[1].split())) for l in f.readlines()])
        else:
            tds = zip(*[[int("".join(l.split(":")[1].split()))] for l in f.readlines()])

        for t, d in tds:
            pos = floor((t + sqrt(t**2 - 4 * (d + 1))) / 2)
            neg = ceil((t - sqrt(t**2 - 4 * (d + 1))) / 2)
            res *= pos - neg + 1

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, "p1")
    res2 = solution(input_dir, output_dir, "p2")
    print(res1)
    print(res2)


if __name__ == "__main__":
    # print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()
