from pathlib import Path


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_15_input.txt"

    with open(input_file, "r") as f:
        data = f.read().strip().split(",")

    res = 0
    boxes = {i: {} for i in range(256)}

    for d in data:
        hsh = 0
        for ix, c in enumerate(d):
            if not p1 and c in ("=", "-"):
                break
            hsh = ((hsh + ord(c)) * 17) % 256
        res += hsh

        d, n = d.split(c)
        box = boxes[hsh]

        if c == "-": box.pop(d, None)
        elif c == "=": box |= {d: int(n)}

    if p1: return res

    res = 0
    for b, l in boxes.items():
        for ix, (_, v) in enumerate(l.items()):
            res += (b + 1) * (ix + 1) * (v)

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
