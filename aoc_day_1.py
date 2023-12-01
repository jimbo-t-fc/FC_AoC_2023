from  get_input_file import get_lines

translation_dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def word_to_digit(line):
    output = line.lower()
    min_num_locations = dict()
    max_num_locations = dict()
    for k in translation_dict.keys():
        if output.find(k) >= 0:
            min_num_locations[k] = output.find(k)
            max_num_locations[k] = max([index for index in range(len(output)) if output.startswith(k, index)])
    if len(min_num_locations) > 0:

        first_word_num = min(min_num_locations, key=min_num_locations.get)
        last_word_num =  max(max_num_locations, key=max_num_locations.get)
        output = output[:min_num_locations[first_word_num]] + translation_dict[first_word_num] + output[min_num_locations[
                                                                                                        first_word_num]:
                                                                                                    max_num_locations[
                                                                                                        last_word_num] + len(
                                                                                                        last_word_num)] + \
                 translation_dict[last_word_num] + output[max_num_locations[last_word_num] + len(last_word_num):]


    return output

if __name__ == '__main__':
    input_1 = get_lines(day_number=1,level_number=1)
    output_1 = sum([int(''.join(c for c in line if c.isdigit())[0]+''.join(c for c in line if c.isdigit( ))[-1]) for line in input_1])
    input_2 = get_lines(day_number=1,level_number=2)
    output_2 = sum([int(''.join(c for c in line if c.isdigit())[0] + ''.join(c for c in line if c.isdigit())[-1]) for line in [word_to_digit(line) for line in input_2]])

    print(f'output 1 = {output_1}')
    print(f'output 2 = {output_2}')


