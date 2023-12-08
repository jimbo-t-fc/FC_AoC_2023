card_score_p1 = {
    'A': '14','K': '13','Q': '12','J': '11','T': '10','9': '09'
    ,'8': '08','7': '07','6': '06','5': '05','4': '04','3': '03','2': '02'
    }

card_score_p2 = {
    'A': '14','K': '13','Q': '12','J': '01','T': '10','9': '09'
    ,'8': '08','7': '07','6': '06','5': '05','4': '04','3': '03','2': '02'
    }


def score_game(cards, pt=1):
    if pt == 2:
        score = [card_score_p2[card] for card in cards]
        Js = cards.count('J')
        if Js == 5:
            return int('6'+''.join(score))
        dupes = {card: cards.count(card)+Js for card in cards if card != 'J'}
    else:
        score = [card_score_p1[card] for card in cards]
        dupes = {card: cards.count(card) for card in cards}
    
    check = {card: cards.count(card) for card in cards}

    # 5 of a kind
    if len(dupes) == 1:
        score.insert(0,'6')
    # 4 of a kind
    elif [1 for _, cnt in dupes.items() if cnt == 4]:
        score.insert(0,'5')
    # Full house
    elif sum([cnt for _, cnt in dupes.items() if cnt == 2 or cnt == 3]) > 4 and len(dupes)==2:
        score.insert(0,'4')
    # 3 of a kind
    elif [1 for _, cnt in dupes.items() if cnt == 3]:
        score.insert(0, '3')
    # 2 pair
    elif sum([1 for _, cnt in dupes.items() if cnt == 2]) > 1 and len(check)==3:
        score.insert(0, '2')
    # 1 pair
    elif [1 for _, cnt in dupes.items() if cnt == 2]:
        score.insert(0,'1')
    return int(''.join(score))


def main():
    with open("2023/Day 7/input.txt",'r') as f:
        lines = [line for line in f.read().split('\n') if line!='']
        
    games = dict([(score_game(list(line.split(" ")[0])), int(line.split(" ")[1])) for line in lines])
    print(f"Part 1: {sum([(idx+1)*games[i] for idx, i in enumerate(sorted(games.keys()))])}")

    games = dict([(score_game(list(line.split(" ")[0]),pt=2), (line.split(" ")[0], int(line.split(" ")[1]))) for line in lines])
    print(f"Part 2: {sum([(idx+1)*games[i][1] for idx, i in enumerate(sorted(games.keys()))])}")

    return


if __name__ == "__main__":
   #import timeit
   #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
   main()