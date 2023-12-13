import copy
from multiprocessing import Pool
#from functools import lru_cache

#@lru_cache
def find_combinations(springs, groups):
    print(f"Springs: {springs}")
    springs = list('.'.join(list(filter(None,springs.split('.')))))
    groups = list(map(int, groups.split(",")))
    pot_combs = [[0]]
    for spring in springs:
        if spring == '#':
            for comb in pot_combs:
                comb[-1] += 1
        elif spring == '?':
            option = copy.deepcopy(pot_combs)
            for comb in pot_combs: # treat as #
                comb[-1] += 1
            option = [comb for comb in option if len(comb)<=len(groups)+1]
            for comb in option: # treat as .
                if comb[-1]>0:
                    comb.append(0)
            pot_combs += option
        elif spring == '.':
            pot_combs = [comb for comb in pot_combs if len(comb)<=len(groups)+1]
            for comb in pot_combs:
                if comb[-1]>0:
                    comb.append(0)
    pass
    return sum([y for y in x if y>0]==groups for x in pot_combs)


def main():
    with open("2023/Day 12/input.txt",'r') as f:
        lines = [[line.split()[0], line.split()[1]] for line in f.read().split('\n') if line!='']
    
    with Pool(9) as p:
        pt1 = sum(p.starmap(find_combinations, lines))
        print(f"Part 1: {pt1}")
        pt2 = sum(p.starmap(find_combinations, [(str(line[0]+'?')*5, line[1]*5) for line in lines]))
        #pt2 = sum(find_combinations(str(line[0]+'?')*5, line[1]*5) for line in lines)
        print(f"Part 2: {pt2}")
    return


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()