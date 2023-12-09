def diffs(seq):
    if len(seq) <= 1:
        return []
    else:
        return [seq[1]-seq[0]] + diffs(seq[1:])

def extrapolate(seq):
    diff_list = diffs(seq)
    if len(set(diff_list)) == 1:
        return seq[-1]+diff_list[0]
    else:
        seq += [seq[-1]+extrapolate(diff_list)]
    return seq[-1]


def main():
    with open("2023/Day 9/input.txt",'r') as f:
        lines = [line for line in f.read().split('\n') if line!='']
    
    pt1 = sum([extrapolate([int(x) for x in seq.split()]) for seq in lines])
    print(f"Part 1: {pt1}")

    pt2 = sum([extrapolate([int(x) for x in reversed(seq.split())]) for seq in lines])
    print(f"Part 2: {pt2}")
    return


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()