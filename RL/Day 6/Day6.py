import math

def race_options(t, d):
    return sum([1 for x in range(1,t) if d - x*(t-x) < 0])


def main():
    with open("2023/Day 6/input.txt",'r') as f:
        lines = [line.split(":")[1].split() for line in f.read().split('\n') if line!='']

    print(f"Part 1: {math.prod(race_options(int(r[0]),int(r[1])) for r in list(zip(lines[0],lines[1])))}")
    print(f"Part 2: {race_options(int(''.join(lines[0])),int(''.join(lines[1])))}")


if __name__ == "__main__":
    main()