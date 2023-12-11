UP, DOWN, LEFT, RIGHT = (-1,0), (1,0), (0,-1), (0,1)
moves = {
    '|': (UP,DOWN)
    ,'-': (LEFT,RIGHT)
    ,'L': (UP,RIGHT)
    ,'J': (UP,LEFT)
    ,'7': (LEFT,DOWN)
    ,'F': (DOWN,RIGHT)
}

next_move = {
    UP: {'7':(-1,-1),'|':(-2,0),'F':(-1,1)}
    ,LEFT: {'L':(-1,-1),'F':(1,-1),'-':(0,-2)}
    ,RIGHT: {'-':(0,2),'7':(1,1),'J':(-1,1)}
    ,DOWN: {'J':(1,-1),'|':(2,0),'L':(1,1)}
}

def find_first_move(array, pos, prev_pipe):
    for pot_pipe_dir, pot_moves in next_move.items():
        if array[pos[0]+pot_pipe_dir[0]][pos[1]+pot_pipe_dir[1]] in pot_moves.keys() and \
            tuple(map(sum, zip(pos, pot_moves[array[pos[0]+pot_pipe_dir[0]][pos[1]+pot_pipe_dir[1]]]))) != prev_pipe:
            return tuple(map(sum, zip(pos, pot_moves[array[pos[0]+pot_pipe_dir[0]][pos[1]+pot_pipe_dir[1]]]))) \
                ,(pos[0]+pot_pipe_dir[0], pos[1]+pot_pipe_dir[1]) \
                ,pot_pipe_dir


def find_next_pos(pos, prev_pos, pipe):
    if tuple(map(sum, zip(pos, moves[pipe][0]))) != prev_pos:
        return tuple(map(sum, zip(pos, moves[pipe][0]))), pos
    else:
        return tuple(map(sum, zip(pos, moves[pipe][1]))), pos

def traverse(array, s_pos):
    cw, prev_cw_pipe, cw_dir = find_first_move(array, s_pos, s_pos)
    acw, prev_acw_pipe, acw_dir = find_first_move(array, s_pos, cw)
    array[s_pos[0]][s_pos[1]] = {pipe for pipe in moves if moves[pipe] in [(cw_dir,acw_dir), (acw_dir,cw_dir)]}.pop()
    history = {s_pos, cw, prev_cw_pipe, acw, prev_acw_pipe}
    cnt = 2
    while True:
        cw, prev_cw_pipe = find_next_pos(cw, prev_cw_pipe, array[cw[0]][cw[1]])
        history.add(cw)
        if cw == acw:
            return cnt, history
        acw, prev_acw_pipe = find_next_pos(acw, prev_acw_pipe, array[acw[0]][acw[1]])
        history.add(acw)
        cnt += 1
        if cw == acw:
            return cnt, history     


def find_nest(array, history):
    nest_size = 0
    nest = []
    enclosed = False
    for x in range(len(array[0])):
        for y, line in enumerate(array):
            if (y,x) not in history:
                if enclosed:
                    nest.append((y,x))
                    nest_size+=1
                continue
            if line[x] == '-':
                enclosed = not enclosed
            elif line[x] in 'F7':
                source_dir = RIGHT if line[x] == 'F' else LEFT
            elif line[x] in 'LJ':
                target_dir = RIGHT if line[x] == 'L' else LEFT
                if target_dir != source_dir:
                    enclosed = not enclosed
    return nest_size, nest


def print_history(array, history, nest=None):
    for y, line in enumerate(array):
        for x, pipe in enumerate(line):
            if (y,x) in nest:
                print("@", end="")
            elif (y,x) in history:
                print(pipe, end="")
            else:
                print('.', end="")
        print("")

def main():
    with open("2023/Day 10/input.txt",'r') as f:
        array = [list(line) for line in f.read().split('\n') if line!='']

    s_pos = [(y, x) for y, line in enumerate(array) for x, val in enumerate(line) if val=='S'][0]
    pt1, history = traverse(array, s_pos)
    print(f"Part 1: {pt1}")

    pt2, nest = find_nest(array, history)
    #print_history(array, history, nest)
    print(f"Part 2: {pt2}")
    return


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()