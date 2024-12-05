from pathlib import Path
from igraph import Graph


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_25_input.txt"

    with open(input_file, "r") as f:
        data = {}
        for l in f.read().split("\n"):
            start, *ends = l.replace(": ", " ").split()
            data[start] = ends
        graph = Graph.ListDict(data)

    min_cuts = graph.mincut().sizes()
    res = min_cuts[0] * min_cuts[1]

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
