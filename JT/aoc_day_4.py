from get_input_file import get_lines

if __name__ == '__main__':

    input_1 = get_lines(day_number=4, level_number=1, test=False)

    print('answer 1 = ', int(sum([2**(len({int(winning_number) for winning_number in line.split('|')[0].split(':')[1].strip().split(' ') if winning_number}.intersection({int(my_number) for my_number in line.split('|')[1].strip().split(' ') if my_number}))-1)//1 for line in input_1 ])))

    card_counter = {card_num:1 for card_num in range(len(input_1))}
    for i, line in enumerate(input_1):
        matches = len({int(winning_number) for winning_number in line.split('|')[0].split(':')[1].strip().split(' ') if
             winning_number}.intersection(
            {int(my_number) for my_number in line.split('|')[1].strip().split(' ') if my_number}))
        for j in range(i+1,min(i+matches+1,max(card_counter)+1)):
            card_counter[j] += card_counter[i]

    print('answer 2 = ', sum(card_counter.values()))
)