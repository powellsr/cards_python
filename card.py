class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
        
    def __repr__(self):
        return self.number + " of " + self.suit
    
    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, suit):
        if suit.lower() in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("Error: Not a valid suit");
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if number.upper() in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number.upper()
        else:
            print("Error: Not a valid card value. Use one-letter abbreviations for face cards.")
        
        
#my_card = Card("hearts", "6")

#print(my_card.suit)
#print(my_card.number)

#my_card.suit = 'dragon'
#my_card.suit = 'clubs'

#my_card.number = '102'
#my_card.number = 'a'

#print(my_card)