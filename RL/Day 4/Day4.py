def part_1(cards):
    return sum([2 ** (len(card[0]) - 1) for _, card in cards.items() if len(card[0]) > 0])


def part_2(cards):
    for i, card in cards.items():
        for _ in range(card[1]):
            for num in range(len(card[0])):
                cards[i+num+1][1] += 1
    return sum(n[1] for _,n in cards.items())


if __name__ == '__main__':
    # Read the input file
    with open("2023/Day 4/input.txt",'r') as f:
        cards = dict([ \
            ( \
                int(line[line.index(' '):line.index(':')]) \
                , [ \
                    set(line[line.index(':')+2:].split('|')[0].strip().replace('  ',' ').split(' ')).intersection( \
                    set(line[line.index(':')+2:].split('|')[1].strip().replace('  ',' ').split(' '))) \
                    ,1] \
            ) for line in f.read().split('\n') if line!=''])

    print(f"Part 1: {part_1(cards)}")    
    
    print(f"Part 2: {part_2(cards)}")