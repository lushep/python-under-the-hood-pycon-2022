class Dealer():
    
    def __init__(self, deck, num_cards=0):
        self._deck = deck
        shuffle(self._deck)
        self._num_cards = num_cards
        
    def deal_hand(self):
        return [self._deck.deal() for n in range(self._num_cards)]

gofish = Dealer(French52Deck(), 7)

gofish.deal_hand()