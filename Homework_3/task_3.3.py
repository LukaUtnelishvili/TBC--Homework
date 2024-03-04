import random
symbols = ['♣', '♦', '♥',  '♠']
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
def print_random_card():
    symb = random.choice(symbols)
    rank = random.choice(ranks)
    print(rank + symb)
for _ in range(1):
    print_random_card()
    