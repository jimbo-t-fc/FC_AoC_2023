from pathlib import Path


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_21_input.txt"

    with open(input_file, "r") as f:
        data = {}
        s = 0
        for y, r in enumerate(f.read().split("\n")):
            for x, v in enumerate(r):
                if v == "#":
                    continue
                data[complex(x, -y)] = v
                if v == "S":
                    s = complex(x, -y)

    lenx = x + 1
    dirs = (1j, -1j, 1, -1)
    num_steps = [64] if p1 else [lenx // 2 + i * lenx for i in range(3)]

    res = []
    cur = {s}
    cnt = 0
    while len(res) != len(num_steps):
        cnt += 1
        cur = {
            p + d
            for d in dirs
            for p in cur
            if complex((p + d).real % lenx, (p + d).imag % -lenx) in data
        }
        if cnt in num_steps:
            res.append(len(cur))

    if p1:
        return res[0]
    else:
        tot = 26501365
        n = tot // 131 + 1
        a = ((res[2] - res[1]) - (res[1] - res[0])) // 2
        b = res[1] - res[0] - 3 * a
        c = res[0] - b - a
        return a * n**2 + b * n + c


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
