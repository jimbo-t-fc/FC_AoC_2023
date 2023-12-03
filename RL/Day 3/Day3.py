def index_array(array):
    num_pos = {}
    sym_pos = []
    star_pos = []
    num_id = 0
    for y, row in enumerate(array):
        num_last = False
        num = ''
        for x, char in enumerate(row):
            if char.isnumeric():
                num+=char
                num_last = True
            elif num_last:
                for i in range(len(num)):
                    num_pos[(y,x-i-1)] = (int(num), num_id)
                num_id+=1
                num_last=False
                num=''
            if not char.isalnum() and char != '.':
                sym_pos.append((y,x))
                if char == '*':
                    star_pos.append((y,x))
        if num_last:
            for i in range(len(num)):
                num_pos[(y,x-i-1)] = (int(num), num_id)
            num_id+=1
            num=''
    return num_pos, sym_pos, star_pos


if __name__ == '__main__':
    # Read the input file
    with open("2023/Day 3/input.txt",'r') as f:
        array = [list(line) for line in f.read().split('\n') if line!='']

    num_pos, sym_pos, star_pos = index_array(array)
    
    parts=set()
    for pos, num in num_pos.items():
        for i in (-1,0,1):
            for j in (-1,0,1):
                if (pos[0]+i,pos[1]+j) in sym_pos:
                    parts.add(num)

    print(f"Part 1: {sum(num for num, id in parts)}")

    gear_ratios=[]
    for pos in star_pos:
        parts=set()
        for i in (-1,0,1):
            for j in (-1,0,1):
                if (pos[0]+i,pos[1]+j) in num_pos.keys():
                    parts.add(num_pos[pos[0]+i,pos[1]+j])
        if len(parts)==2:
            gear_ratios.append(parts.pop()[0]*parts.pop()[0])
    
    print(f"Part 2: {sum(gear_ratios)}")



    pass