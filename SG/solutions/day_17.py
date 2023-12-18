from pathlib import Path
from heapq import heappop, heappush


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_17_input.txt"

    with open(input_file, "r") as f:
        data = f.read().split("\n")

    queue = [(0, 0, 0, 1), (0, 0, 0, -1j)]
    heats = {0: 0}
    traversed = set()
    tracker = 0

    while queue:
        heat, _, pos, drct = heappop(queue)

        if (pos, drct) in traversed:
            continue
        traversed.add((pos, drct))

        for d in drct * 1j, drct * -1j:
            hi = 0
            for n in range(1, (3 if p1 else 10) + 1):
                new_pos = pos + d * n
                if not (0 <= -new_pos.imag < len(data)) or not (
                    0 <= new_pos.real < len(data[0])
                ):
                    break

                hi += int(data[int(-new_pos.imag)][int(new_pos.real)])
                h = heat + hi

                if not p1 and n < 4:
                    continue

                tracker += 1
                heappush(queue, (h, tracker, new_pos, d))
                if heats.get(new_pos, 10000000000) < h:
                    continue
                heats[new_pos] = h

    return heats[complex(len(data[0]) - 1, -len(data) + 1)]


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
