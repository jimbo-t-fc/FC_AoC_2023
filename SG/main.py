from aocd import get_data
from aocd.get import current_day

if __name__ == "__main__":
    input_fn = f"./input/day_{current_day()}_input.txt"
    print(get_data(), file=open(input_fn, "w"))

    template = f"""from pathlib import Path

def solution(input_dir, output_dir, part):
    input_file = Path(input_dir) / "day_{current_day()}_input.txt"

    res = None
    with open(input_file, "r") as f:
        data = f.read().strip('\\n')

    return res

def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, "p1")
    res2 = solution(input_dir, output_dir, "p2")
    print("Part 1:", res1)
    print("Part 2:", res2)

if __name__ == "__main__":
    main()
"""

    template_fn = f"./solutions/day_{current_day()}.py"
    print(template, file=open(template_fn, "w"))
