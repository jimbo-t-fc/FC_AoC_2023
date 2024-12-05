from pathlib import Path


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_13_input.txt"

    with open(input_file, "r") as f:
        data_rows = [m.split("\n") for m in f.read().split("\n\n")]
        data_cols = [list(map(list, zip(*dr))) for dr in data_rows]

    def smudge(s1, s2):
        return sum(1 for a, b in zip(s1, s2) if a != b) == 1

    res = 0
    for by_rows, data in enumerate((data_cols, data_rows)):
        for mir in data:
            for idx, ml in enumerate(mir):
                if (mls := smudge(ml, mir[idx - 1]) and not p1) or (ml == mir[idx - 1]):
                    match, smudged = True, mls
                    for i in range(idx - 1):
                        ridx = idx + (idx - 1 - i)
                        if ridx < len(mir) and mir[i] != mir[ridx]:
                            if not p1 and not smudged and smudge(mir[i], mir[ridx]):
                                smudged = True
                            else:
                                match = False
                    if match and (p1 or smudged):
                        res += idx * 100 if by_rows else idx

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    res2 = solution(input_dir, output_dir, False)
    print("Part 1:", res1)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
