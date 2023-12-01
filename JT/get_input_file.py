def get_lines(day_number, level_number , test = False):
    if test:
        with open(f'input_files/aoc_day_{day_number}_test_input_{level_number}.txt') as file:
            return file.read().split('\n')
    else:
        with open(f'input_files/aoc_day_{day_number}_input_{level_number}.txt') as file:
            return file.read().split('\n')


