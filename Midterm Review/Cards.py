import random


class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):  # check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # suits are the same... check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # ranks are the same... it's a tie
        return 0

    def count(self):
        if not self.rank:
            value = 0
        elif self.rank == 'Ace':
            value = 1
        elif self.rank == 'Jack':
            value = 11
        elif self.rank == 'Queen':
            value = 12
        elif self.rank == 'King':
            value = 13
        else:
            value = int(self.rank)
        return value


class Deck(object):
    cards = []

    def __init__(self):
        self.cards
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
            return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards) 

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
            

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def show_cards(self):
        for c in self.cards:
            print(c)


deck = Deck()
deck.shuffle()
total = int()
hand = Hand('new hand')
for c in range(5):
    card = deck.pop_card()
    hand.add_card(card)
    total = total + card.count()
hand.show_cards()
print("The total is: {}".format(total))
