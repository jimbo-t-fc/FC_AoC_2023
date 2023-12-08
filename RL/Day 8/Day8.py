import math

def traverse(graph, moves, current_node, end_node, cnt_moves):
    keep_going = True
    while keep_going:
        cnt_moves += 1
        rl = moves.pop(0)
        current_node = graph[current_node][int(rl)]
        moves.append(rl)
        keep_going = current_node[-len(end_node):] != end_node
    return cnt_moves, moves, current_node

# Brute force
def multi_traverse_brute_force(graph, moves):
    ghosts = {k: {'cnt_moves':0, 'moves':moves.copy(), 'current_node':k} for k in graph.keys() if k[-1]=='A'}
    while True:
        for ghost, info in sorted(ghosts.items(), key=lambda item: item[1]['cnt_moves']):
            ghosts[ghost]['cnt_moves'], ghosts[ghost]['moves'], ghosts[ghost]['current_node'] = traverse(graph, info['moves'], info['current_node'], "Z", info['cnt_moves'])
            if len(set([v['cnt_moves'] for _,v in ghosts.items()])) == 1:
                return ghosts[ghost]['cnt_moves']
            
# LCM
def multi_traverse(graph, moves):
    ghosts = {k: {'cnt_moves':0, 'moves':moves.copy(), 'current_node':k} for k in graph.keys() if k[-1]=='A'}
    for ghost, info in sorted(ghosts.items(), key=lambda item: item[1]['cnt_moves']):
        ghosts[ghost]['cnt_moves'], ghosts[ghost]['moves'], ghosts[ghost]['current_node'] = traverse(graph, info['moves'], info['current_node'], "Z", info['cnt_moves'])
    return math.lcm(*[v['cnt_moves'] for _,v in ghosts.items()])


def main():
    with open("2023/Day 8/input.txt",'r') as f:
        lines = [line for line in f.read().split('\n') if line!='']
        
    moves = list(lines[0].replace('R','1').replace('L','0'))
    graph = {line[:3]: (line[7:10], line[-4:-1]) for line in lines[1:]}
    print(f"Part 1: {traverse(graph, moves, 'AAA', 'ZZZ', 0)[0]}")

    graph = {line[:3]: (line[7:10], line[-4:-1]) for line in lines[1:]}
    print(f"Part 2: {multi_traverse(graph, moves)}")



    return


if __name__ == "__main__":
   #import timeit
   #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
   main()