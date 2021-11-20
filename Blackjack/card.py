class Card:
    '''
    A card class to create cards for the game.
    It has 2 attributes - Suit & Rank
    It also has method print which can print the card suit & rank
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

# sample_card = Card('Hearts', 'Three')
# print(sample_card)