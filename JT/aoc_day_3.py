from get_input_file import get_lines

def find_neighbors(coords):
    x , y = coords
    neighbors = ((i,j) for i in range(x-1,x+2) for j in range(y-1,y+2))
    return neighbors

def complete_number(coords, digit_locations):
    complete_number = digit_locations[coords]
    complete_num_coords = [coords]
    x , y = coords
    while True:
        x += 1
        if digit_locations.get((x,y), "False").isdigit():
            complete_number = complete_number + digit_locations[(x,y)]
            complete_num_coords.append((x,y))
        else:
            break
    x , y = coords
    while True:
        x -= 1
        if digit_locations.get((x,y), "False").isdigit():
            complete_number = digit_locations[(x,y)] + complete_number
            complete_num_coords = [(x,y)] + complete_num_coords
        else:
            break
    return [complete_number, complete_num_coords]

def find_numbers(neighbors, digit_locations):
    connected_numbers ,checked_coords = [], []
    for coord in neighbors:
        if coord in digit_locations:
            connected_number, checked_coord = complete_number(coord, digit_locations)
            if checked_coord not in checked_coords:
                checked_coords.append(checked_coord)
                connected_numbers.append(int(connected_number))
    return connected_numbers

if __name__ == '__main__':

    input_1 = get_lines(day_number=3, level_number=1, test=False)

    digit_locations = {(x_coord, y_coord):char for y_coord, line in enumerate(input_1) for x_coord, char in enumerate(line) if char.isdigit()}
    symbol_locations = {(x_coord, y_coord):char for y_coord, line in enumerate(input_1) for x_coord, char in enumerate(line) if not char.isdigit() and char != '.'}

    output_1  = sum([sum(find_numbers(find_neighbors(coords), digit_locations)) for coords, symbol in symbol_locations.items()])

    print(output_1)
    output_2 = sum([find_numbers(find_neighbors(coords), digit_locations)[0]*find_numbers(find_neighbors(coords), digit_locations)[1] for coords, symbol in symbol_locations.items() if len(find_numbers(find_neighbors(coords), digit_locations))==2])

    print(output_2)
