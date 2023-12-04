from pathlib import Path
from collections import defaultdict
import timeit


def solution(input_dir, output_dir):
    input_file = Path(input_dir) / "day_4_input.txt"

    with open(input_file, "r") as f:
        score = scratchcards = 0
        copies = defaultdict(int)

        for scn, sc in enumerate(f.readlines()):
            tot_cards = copies[scn] + 1
            scratchcards += tot_cards

            w_nums, a_nums = (set(n.split()) for n in sc.split(":")[1].split("|"))
            wins = len(w_nums & a_nums)
            if wins > 0:
                score += 2 ** (wins - 1)  # p1
                for w in range(wins):
                    copies[scn + w + 1] += tot_cards  # p2

    return score, scratchcards


def main(input_dir="../input", output_dir="../output"):
    res1, res2 = solution(input_dir, output_dir)
    print(res1)
    print(res2)


if __name__ == "__main__":
    # print(sum(timeit.repeat(main, number=1000, repeat=3)) / 3 / 1000)
    main()
