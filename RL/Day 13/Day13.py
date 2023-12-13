def transpose(ls):
    nls = ['' for _ in range(len(ls[0]))]
    for st in ls:
        for j, ch in enumerate(st):
            nls[j] += ch
    return nls

def find_reflection(pattern):
    for i in range(1,len(pattern)//2+1):
        if pattern[:i][::-1]==pattern[i:i+i]:
            return i
    for i in range(len(pattern)//2+1, len(pattern)):
        if pattern[i:][::-1]==pattern[i-(len(pattern)-i):i]:
            return i
    return 0

def find_reflection_with_smudge(pattern):
    for i in range(1,len(pattern)//2+1):
        diff = 0
        for j in range(i):
            diff += sum(1 for x,ch in enumerate(list(pattern[:i][::-1][j])) if ch!=list(pattern[i:i+i][j])[x])
        if diff == 1:
            return i
    for i in range(len(pattern)//2+1, len(pattern)):
        diff = 0
        for j in range(len(pattern[i:][::-1])):
            diff += sum(1 for x,ch in enumerate(list(pattern[i:][::-1][j])) if ch!=list(pattern[i-(len(pattern)-i):i][j])[x])
        if diff == 1:
            return i
    return 0

def main():
    with open("2023/Day 13/input.txt",'r') as f:
        patterns = [pattern.split('\n') for pattern in f.read().split('\n\n')]
    
    pt1 = 0
    for pattern in patterns:
        pt1 += 100*find_reflection(pattern)
        pt1 += find_reflection(transpose(pattern))
    print(f"Part 1: {pt1}")

    pt2 = 0
    for pattern in patterns:
        pt2 += 100*find_reflection_with_smudge(pattern)
        pt2 += find_reflection_with_smudge(transpose(pattern))
    print(f"Part 2: {pt2}")
    return


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()