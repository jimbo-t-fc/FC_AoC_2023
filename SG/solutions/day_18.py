from pathlib import Path


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_18_input.txt"

    with open(input_file, "r") as f:
        data = f.read().split("\n")

    res = 0
    cur = 0
    p = 0
    coords = [0]
    directions = {"U": 1j, "D": -1j, "R": 1, "L": -1}
    for d in data:
        dr, ln, col = d.split()
        if not p1:
            dr = col[-2].translate(str.maketrans("0123", "RDLU"))
            ln = int(col[2:-2], 16)

        direct = directions[dr]
        cur += direct * int(ln)
        p += int(ln)
        coords.append(cur)

    mysum = 0
    for idx, c in enumerate(coords):
        if idx + 1 == len(coords):
            nx = 0
        else:
            nx = idx + 1
        mysum += (coords[nx].imag - c.imag) * (coords[nx].real + c.real)
    mysum = abs(mysum) // 2

    res = mysum + p // 2 + 1

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
