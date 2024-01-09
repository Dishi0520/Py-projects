import random

## coin = random.choice(["heads", "tails"])
# print(coin) 

#number = random.randint(1,10)
# print(number)

#random.shuffle(x): takes a list and shuffles the order

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
#random.randint(a, b): a random interger from A to B inclusive