from pathlib import Path


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_9_input.txt"

    res = 0
    for d in open(input_file).read().split("\n"):
        diffs = [list(map(int, d.split()))[:: (p1 or -1)]]  # p2 = p1 reversed
        for nums in diffs:
            if any(nums):
                diffs.append([j - i for j, i in zip(nums[1:], nums[:-1])])
        res += sum([ds[-1] for ds in diffs])

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    res2 = solution(input_dir, output_dir, False)
    print("Part 1:", res1)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
