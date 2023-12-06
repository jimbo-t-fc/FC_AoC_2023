def find_next_seeds_1(seeds, maps):
    new_seeds = seeds
    for seed in seeds:
        for map in maps:
            m = map.split()
            dest, source, span = int(m[0]), int(m[1]), int(m[2])
            if source <= seed < source+span:
                new_seeds.remove(seed)
                new_seeds.append(dest+(seed-source))
                break
    return new_seeds


def find_next_seeds_2(seeds, maps):
    new_seeds = []
    for idx, s in enumerate(seeds):
        for map in maps:
            m = map.split()
            dest, source, span = int(m[0]), int(m[1]), int(m[2])
            #         source  source+span
            # map:       |-----|
            #     s[0]  s[0]+s[1]
            # seed: |------|
            if s[0] < source and source <= s[0]+s[1] <= source+span:
                seeds[idx] = (s[0], source-s[0]-1)
                new_seeds.append((dest, (s[0]+s[1])-source))
                s = ((s[0], source-s[0]-1))
            #         source  source+span
            # map:       |-----|
            #               s[0]  s[0]+s[1]
            # seed:          |------|
            elif source <= s[0] < source+span and source+span <= s[0]+s[1]: #might be < at the end
                new_seeds.append((dest+(s[0]-source), span-(s[0]-source)-1))
                seeds[idx] = (source+span, (s[0]+s[1])-(source+span))
                s = ((source+span, (s[0]+s[1])-(source+span)))
            #         source  source+span
            # map:       |--------|
            #           s[0]  s[0]+s[1]
            # seed:       |------|
            elif source <= s[0] < source+span and source <= s[0]+s[1] < source+span:
                new_seeds.append((dest+(s[0]-source), s[1]))
                seeds[idx] = -1
                break
            #         source  source+span
            # map:         |-----|
            #           s[0]  s[0]+s[1]
            # seed:      |---------|
            elif s[0] < source and source+span <= s[0]+s[1]:
                seeds[idx] = (s[0], source-s[0]-1)
                new_seeds.append((dest, span))
                seeds.append((source+span, (s[0]+s[1])-(source+span)))
                s = ((s[0], source-s[0]-1))
        
    new_seeds += [seed for seed in seeds if seed!=-1]

    return new_seeds


def main():
     # Read the input file
    with open("2023/Day 5/input.txt",'r') as f:
        sections = [section for section in f.read().split('\n\n')]
    
    # PART 1
    seeds = [int(x) for x in sections[0].split(':')[1].split()]
    for mapping in sections[1:]:
        seeds = find_next_seeds_1(seeds,mapping.split('\n')[1:])
    print(f"Part 1: {min(seeds)}")

    # PART 2
    seeds = [int(x) for x in sections[0].split(':')[1].split()]
    seeds_2 = list(zip(seeds[::2], seeds[1::2]))
    for mapping in sections[1:]:
        seeds_2 = find_next_seeds_2(seeds_2,mapping.split('\n')[1:])
    print(f"Part 2: {min([seed[0] for seed in seeds_2])}")


if __name__ == '__main__':
   main()