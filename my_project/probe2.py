from itertools import cycle

def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет",
                   "дама", "король", "туз"]
    card_mast = ["пик", "треф", "бубен", "червей"]
    card_mast = cycle([i for i in card_mast if i != suit])


    for mast in card_mast:
        for val in card_values:
            yield f'{val} {mast}'




generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)