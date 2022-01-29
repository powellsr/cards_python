from card import Card

class Deck:
    
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)
        
    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(suit, num) for suit in suits for num in numbers]
        
    def shuffle(self):
        return self._cards
        
    def euchre(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(9, 11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(suit, num) for suit in suits for num in numbers]
#my_deck = Deck()
