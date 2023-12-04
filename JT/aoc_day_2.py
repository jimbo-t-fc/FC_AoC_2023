from  get_input_file import get_lines

if __name__ == '__main__':

    input_1 = get_lines(day_number=2,level_number=1,test=False)
    ###########################################################
    # Method 1 - less efficient I think
    ###########################################################
    
    game_details = {l.split(': ')[0]:{f'set_{i}':{cube.split(' ')[1]:int(cube.split(' ')[0]) for cube in _set.split(', ')} for i,  _set in enumerate(l.split(': ')[1].split('; '))} for l in input_1}

    # Part 1
    possible_id_sum = 0
    for game_name , details in game_details.items():
        for cubes in details.values():
            if ('red' in cubes and cubes['red'] > 12) or ('green' in cubes and cubes['green'] > 13) or ('blue' in cubes and cubes['blue'] > 14):
                break
        else:
            possible_id_sum += int(game_name.split(' ')[1])

    # Part 2
    power_sum = 0
    for game_name, details in game_details.items():
        max_colours = {'red':0,'green':0,'blue':0}
        for cubes in details.values():
            for colour in ('red','green','blue'):
                if colour in cubes and cubes[colour] > max_colours[colour]:
                    max_colours[colour] = cubes[colour]
        power_sum += max_colours['red']*max_colours['green']*max_colours['blue']

    print(f'output 1 = {possible_id_sum}')
    print(f'output 2 = {power_sum}')

    ###########################################################
    # Method 2 - more efficient
    ###########################################################
    new_game_details = {l.split(': ')[0]:{'red':[int(data.split(' ')[0]) for data in [cube for cubes in [_set.split(', ') for _set in  l.split(': ')[1].split('; ')] for cube in cubes] if data.split(' ')[1] == 'red'],\
                                          'green':[int(data.split(' ')[0]) for data in [cube for cubes in [_set.split(', ') for _set in  l.split(': ')[1].split('; ')] for cube in cubes] if data.split(' ')[1] == 'green'],\
                                          'blue':[int(data.split(' ')[0]) for data in [cube for cubes in [_set.split(', ') for _set in  l.split(': ')[1].split('; ')] for cube in cubes] if data.split(' ')[1] == 'blue']}\
                                            for l in input_1}

    possible_id_sum = 0
    for game_name , details in new_game_details.items():
        if ('red' in details and max(details['red']) <= 12) and ('green' in details and max(details['green']) <= 13) and ('blue' in details and max(details['blue']) <= 14):
            possible_id_sum += int(game_name.split(' ')[1])

    power_sum = 0
    for details in new_game_details.values():
        max_colours = {'red': 0, 'green': 0, 'blue': 0}
        for colour, values in details.items():
            max_colours[colour] = max(values)
        power_sum += max_colours['red'] * max_colours['green'] * max_colours['blue']

    print(f'output 1 = {possible_id_sum}')
    print(f'output 2 = {power_sum}')
