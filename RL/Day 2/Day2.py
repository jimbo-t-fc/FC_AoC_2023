def cube_info(cubes):
    picks=[]
    for handful in cubes:
        cube_info={'blue':0,'green':0,'red':0}
        for colour in handful.split(','):
            ele = colour.split(' ')
            cube_info[ele[2]] = int(ele[1])
            picks.append(cube_info)
    return picks

if __name__ == '__main__':
    # Read the input file
    with open("2023/Day 2/input.txt",'r') as f:
        lines = [tuple(line.split(":")) for line in f.read().split('\n') if line!='']
    
    games = dict((int(x.replace("Game ","")),cube_info(y.split(";"))) for x,y in lines)

    sum = 0
    for game_id, handfuls in games.items():
        possible = True
        for handful in handfuls:
            if handful['blue']>14 or handful['red']>12 or handful['green']>13:
                possible = False

        if possible:
            sum+=game_id

    print(f'Part 1: {sum}')

    sum = 0
    for game_id, handfuls in games.items():
        minblue, mingreen, minred = 0, 0, 0
        for handful in handfuls:
            minblue = max(minblue,handful['blue'])
            mingreen = max(mingreen,handful['green'])
            minred = max(minred,handful['red'])

        power = minblue*mingreen*minred
        sum += power

    print(f'Part 2: {sum}')

    pass