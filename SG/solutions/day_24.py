from pathlib import Path
import z3


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_24_input.txt"

    with open(input_file, "r") as f:
        data = []
        for l in f.read().split("\n"):
            data.append(list(map(int, l.replace(" @ ", ", ").split(", "))))

    target_x = target_y = (200000000000000, 400000000000000)
    res = 0

    if p1:
        for idx, d1 in enumerate(data):
            for d2 in data[idx + 1 :]:
                if d1 == d2:
                    continue
                x1, y1, z1, vx1, vy1, vz1 = d1
                x2, y2, z2, vx2, vy2, vz2 = d2
                slope1 = vy1 / vx1
                slope2 = vy2 / vx2
                int1 = y1 - slope1 * x1
                int2 = y2 - slope2 * x2

                if slope1 == slope2:
                    continue

                xint = (int2 - int1) / (slope1 - slope2)
                yint = slope1 * xint + int1

                t1 = (xint - x1) / vx1
                t2 = (xint - x2) / vx2

                if t1 < 0 or t2 < 0:
                    continue

                if (target_x[0] <= xint <= target_x[1]) and (
                    target_y[0] <= yint <= target_y[1]
                ):
                    res += 1
    else:
        x, y, z, vx, vy, vz = z3.Reals("x y z vx vy vz")
        solver = z3.Solver()

        for idx, h in enumerate(data[:3]):
            tK = z3.Real(f"t{idx}")
            solver.add(tK > 0)
            solver.add(x + tK * vx == h[0] + tK * h[3])
            solver.add(y + tK * vy == h[1] + tK * h[4])
            solver.add(z + tK * vz == h[2] + tK * h[5])
        solver.check()
        res = sum(solver.model()[var].as_long() for var in [x, y, z])

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
