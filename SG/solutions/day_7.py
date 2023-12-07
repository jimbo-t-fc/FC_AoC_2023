from pathlib import Path
from collections import Counter


def solution(input_dir, output_dir, part):
    input_file = Path(input_dir) / "day_7_input.txt"
    with open(input_file, "r") as f:
        data = f.read().strip("\n").split("\n")

    def compare_hands(hand):
        ho = "AKQJT98765432" if part == "p1" else "AKQT98765432J"
        return [ho.index(c) for c in hand[0]]

    ranks = {i: [] for i in range(4, -5, -1)}

    for hs in data:
        h, b = hs.split()
        c = Counter(list(h))

        if part == "p2":
            jc = c.pop("J", None)
            mck = c.most_common(1)[0][0] if c else "J"
            c[mck] += jc if jc else 0

        mc, cl = c.most_common(1)[0], len(c)
        ranks[mc[1] - cl].append((h, b))

    res, rank = 0, len(data)
    for rl in ranks.values():
        rl.sort(key=compare_hands)
        for h in rl:
            res += int(h[1]) * rank
            rank -= 1

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, "p1")
    res2 = solution(input_dir, output_dir, "p2")
    print("Part 1:", res1)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
