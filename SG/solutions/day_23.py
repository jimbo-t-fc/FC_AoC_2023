from pathlib import Path
from collections import deque


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_23_input.txt"

    with open(input_file, "r") as f:
        data = {}
        for y, l in enumerate(f.read().split("\n")):
            for x, v in enumerate(l):
                if v != "#":
                    data[complex(x, -y)] = v

    lenx, leny = x, y
    dirs = {"^": 1j, "v": -1j, "<": -1, ">": 1}
    nxt_data = {}
    for d, v in data.items():
        if p1 and v in dirs:
            nxdrs = [dirs[v]]
        else:
            nxdrs = list(dirs.values())

        nxt_data[d] = [(d + nd, nd, 1) for nd in nxdrs if d + nd in data]

    def collapse(p, n, dr, d=1):
        while len(nxt_data[n]) == 2:
            p, n, d = n, [*{*[n[0] for n in nxt_data[n]]} - {p}][0], d + 1
        return n, dr, d

    if not p1:
        nxt_data = {p: [collapse(p, n, dr) for n, dr, d in nxt_data[p]] for p in data}

    s = [d for d in data if d.imag == 0][0]
    e = [d for d in data if d.imag == -leny][0]

    q = deque([(s, 0)])
    c = {}
    es = []
    visited = set()
    while q:
        cur, st = q.pop()

        if st == -1:
            visited.remove(cur)
            continue

        if cur in visited:
            continue

        if cur == e:
            es.append(st)
            continue

        visited.add(cur)
        q.append((cur, -1))

        v = data[cur]

        for nxt, d, stps in nxt_data[cur]:
            if nxt in data:
                q.append((nxt, st + stps))

    res = max(es)
    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
