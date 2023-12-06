from pathlib import Path
import timeit


def merge_ranges(initial, compare, replacement_start):
    mapped = []
    unmapped = []

    if (sum(initial) <= compare[0]) or (initial[0] >= sum(compare)):
        unmapped.append(initial)
    else:
        if initial[0] < compare[0]:
            unmapped.append((initial[0], compare[0] - initial[0]))
        if sum(initial) >= sum(compare):
            unmapped.append((sum(compare), sum(initial) - sum(compare)))

        mapped.append(
            (
                replacement_start + max(initial[0], compare[0]) - compare[0],
                min(sum(initial), sum(compare)) - max(initial[0], compare[0]),
            )
        )

    return unmapped, mapped


def solution(input_dir, output_dir, part):
    input_file = Path(input_dir) / "day_5_input.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()

        all_seeds = [int(s) for s in lines[0].split(":")[1].split()]
        if part == "p1":
            unmapped = [(s, 1) for s in all_seeds]
        else:
            unmapped = list(zip(all_seeds[::2], all_seeds[1::2]))
        mapped = []

        for l in lines[1:]:
            if l.endswith(":\n"):
                unmapped = unmapped + mapped
                mapped = []
            elif l[0].isdigit():
                de, so, rl = map(int, l.split())
                for idx in range(len(unmapped) - 1, -1, -1):
                    ru, rm = merge_ranges(unmapped.pop(idx), (so, rl), de)
                    unmapped += ru
                    mapped += rm

    res = min(unmapped + mapped)[0]

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, "p1")
    res2 = solution(input_dir, output_dir, "p2")
    print(res1)
    print(res2)


if __name__ == "__main__":
    # print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()
