from pathlib import Path
import re

def solution(input_dir, output_dir):
    input_file = Path(input_dir) / "day_10_input.txt"

    with open(input_file, "r") as f:
        data = []
        start = None
        for idx, d in enumerate(f.read().split("\n")):
            if "S" in d:
                start = (idx, d.index("S"))
            data.append(d)

    pipes = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(0, 1), (-1, 0)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }
    
    curs = ((start[0]+1, start[1]), (start[0], start[1]+1), (start[0]-1, start[1]), (start[0], start[1]-1))

    for cur in curs:
        prev = stop = start
        seq = [cur]
        while cur != stop:
            diff = tuple(y-x for x, y in zip(cur, prev))
            tp = data[cur[0]][cur[1]]
            if tp in pipes and diff in pipes[tp]:
                nxt = pipes[tp][0] if pipes[tp][1] == diff else pipes[tp][1]
                prev = cur
                cur = tuple(x+y for x, y in zip(prev, nxt)) 
                seq.append(cur)
            else:
                seq = None
        if seq:
            break
    res1 = len(seq)//2
    
    spipe = None
    for p, c in pipes.items():
        if tuple(x-y for x,y in zip(seq[0], start)) in c:
            if tuple(x-y for x,y in zip(seq[-2], start)) in c:
                spipe = p
                break 
    
    res2 = 0
    for r, row in enumerate(data):
        bends = 0
        for c, col in enumerate(row[::-1]):
            cur = (r, len(row)-1-c)
            if cur in seq:
                if col.replace("S", spipe) in "|F7":
                    bends += 1
            elif bends % 2:
                a += 1

    return res1, res2

def main(input_dir="../input", output_dir="../output"):
    res1, res2 = solution(input_dir, output_dir)
    print("Part 1:", res1)
    print("Part 2:", res2)

if __name__ == "__main__":
    main()