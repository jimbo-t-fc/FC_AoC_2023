import os

def part_1(data):
    
    return None


def part_2(data):
    
    return None


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = f.read().strip().split('\n')
    print(f"Part 1: {part_1(puzzle_data)}")
    print(f"Part 2: {part_2(puzzle_data)}")