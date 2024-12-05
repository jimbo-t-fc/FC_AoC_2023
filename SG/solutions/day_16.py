from pathlib import Path
import sys
from collections import defaultdict

sys.setrecursionlimit(5000)


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_16_input.txt"

    with open(input_file, "r") as f:
        data = f.read().split("\n")

    drcts = {
        ".": lambda d: d,
        "\\": lambda d: complex(-d.imag * (d.real == 0), -d.real * (d.imag == 0)),
        "/": lambda d: complex(d.imag * (d.real == 0), d.real * (d.imag == 0)),
    }

    def beam(cur, prev, drct, passed):
        if not (0 <= -cur.imag < len(data)) or not (0 <= cur.real < len(data[0])):
            return
        if cur in passed and prev in passed[cur]:
            return
        passed[cur].add(prev)

        m = data[int(-cur.imag)][int(cur.real)]
        nxt_drs = []
        if m in ".\\/":
            nxt_drs.append(drcts[m](drct))
        elif m == "|" and drct.real == 0:
            nxt_drs.append(drcts["."](drct))
        elif m == "-" and drct.imag == 0:
            nxt_drs.append(drcts["."](drct))
        else:
            nxt_drs.append(drcts["\\"](drct))
            nxt_drs.append(drcts["/"](drct))

        for nxt_dr in nxt_drs:
            nxt = cur + nxt_dr
            beam(nxt, cur, nxt_dr, passed)
        return

    def do_beam(st, dr):
        all_passed = defaultdict(set)
        beam(st, None, dr, all_passed)
        return len(all_passed)

    if p1:
        res = do_beam(0, 1)
    else:
        all_res = []

        for s in range(len(data[0])):
            for l in ((0, -1j), (len(data[1]) - 1, 1j)):
                all_res.append(do_beam(complex(s, l[0]), l[1]))

        for s in range(len(data)):
            for l in ((0, 1), (len(data) - 1, -1)):
                all_res.append(do_beam(complex(l[0], -s), l[1]))

        res = max(all_res)

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
