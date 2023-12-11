from itertools import combinations


def expand_universe(universe, years_old):
    xc = set(range(min([g[0] for g in universe]), max([g[0] for g in universe])+1))
    yc = set(range(min([g[1] for g in universe]), max([g[1] for g in universe])+1))
    xg = set(g[0] for g in universe)
    yg = set(g[1] for g in universe)
    return [(g[0]+sum(i<g[0] for i in xc-xg)*years_old, g[1]+sum(j<g[1] for j in yc-yg)*years_old) for g in universe]


def galaxy_distance(universe):
    return sum([abs(pair[0][0]-pair[1][0])+abs(pair[0][1]-pair[1][1]) for pair in list(combinations(universe, 2))])

def print_universe(universe):
    for y in range(max([g[1] for g in universe])+1):
        for x in range(max([g[0] for g in universe])+1):
            if (x,y) in universe:
                print("#", end="")
            else:
                print(f'{x}'[-1], end="")
        print("")


def main():
    with open("2023/Day 11/input_test.txt",'r') as f:
        universe = [(x,y) for y, line in enumerate(f.read().split('\n')) if line!='' for x, gc in enumerate(line) if gc=='#']

    expanded_universe = expand_universe(universe, 1)
    pt1 = galaxy_distance(expanded_universe)
    print(f"Part 1: {pt1}")

    expanded_universe = expand_universe(universe, 100)
    pt2 = galaxy_distance(expanded_universe)
    print(f"Part 2: {pt2}")
    return


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()