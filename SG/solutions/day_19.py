from pathlib import Path
from math import prod


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_19_input.txt"

    workflows = {}
    parts = []
    with open(input_file, "r") as f:
        wfs, pts = f.read().split("\n\n")
        for w in wfs.split("\n"):
            wn, rest = w[:-1].split("{")
            workflows[wn] = [r.split(":") for r in rest.split(",")]

        for p in pts.split("\n"):
            new_part = {
                n.split("=")[0]: int(n.split("=")[1]) for n in p[1:-1].split(",")
            }
            parts.append(new_part)

    if p1:
        res = 0
        for p in parts:
            wfn = "in"

            while wfn not in ("A", "R"):
                cur_wf = workflows[wfn]

                for step in cur_wf:
                    r = {"x": p["x"], "m": p["m"], "a": p["a"], "s": p["s"]}
                    if len(step) == 2:
                        ns = f"{{{step[0][0]}}}{step[0][1:]}"
                        if eval(ns.format(**r)):
                            wfn = step[1]
                            break
                    elif len(step) == 1:
                        wfn = step[0]

            if wfn == "A":
                res += sum(p.values())
    else:
        q = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]
        a = []

        while q:
            wfn, rns = q.pop()

            if wfn == "A":
                a.append(rns)
            elif wfn != "R":
                for step in workflows[wfn]:
                    if len(step) == 2:
                        ct, comp, num = step[0][0], step[0][1], int(step[0][2:])
                        nr = {}
                        for rn, r in rns.items():
                            if r == None:
                                break
                            elif rn == ct:
                                if comp == "<":
                                    if r[0] >= num:
                                        break
                                    else:
                                        nr[ct] = (r[0], min(num - 1, r[1]))
                                        rns[ct] = (num, r[1]) if r[1] >= num else None
                                if comp == ">":
                                    if r[1] <= num:
                                        break
                                    else:
                                        nr[ct] = (max(num + 1, r[0]), r[1])
                                        rns[ct] = (r[0], num) if r[0] <= num else None
                            else:
                                nr[rn] = r
                        if len(nr) == 4:
                            q.append((step[1], nr))
                    elif len(step) == 1:
                        if any(r is None for r in rns.values()):
                            break
                        else:
                            q.append((step[0], rns))

        res = sum(prod(r[1] - r[0] + 1 for _, r in rng.items()) for rng in a)

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
