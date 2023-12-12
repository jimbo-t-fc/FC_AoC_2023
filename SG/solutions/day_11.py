from pathlib import Path


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_11_input.txt"

    with open(input_file, "r") as f:
        data = f.read().split("\n")

    ecs = set(range(len(data[0])))
    ers = set(range(len(data)))
    coords = []
    for r, d in enumerate(data):
        for c, l in enumerate(d):
            if l == "#":
                coords.append((r, c))
                if c in ecs:
                    ecs.remove(c)
                if r in ers:
                    ers.remove(r)

    res = 0
    for idx, c1 in enumerate(coords):
        for c2 in coords[idx + 1 :]:
            d = abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])
            for ec in ecs:
                if min(c1[1], c2[1]) < ec < max(c1[1], c2[1]):
                    d += 1 if p1 else 999999
            for er in ers:
                if min(c1[0], c2[0]) < er < max(c1[0], c2[0]):
                    d += 1 if p1 else 999999
            res += d

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    res2 = solution(input_dir, output_dir, False)
    print("Part 1:", res1)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
