class AvatarDeck(Deck):
    ranks = list('23456789') + ['Toph', 'Sokka', 'Katara', 'Zuko', 'Aang']
    suits = ['Water', 'Air', 'Fire', 'Water']
    
    def __init__(self):
        Card = collections.namedtuple('Card', ['rank', 'suit'])
        self._cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
        
avatar_deck = AvatarDeck()
for card in avatar_deck[12::13]:
    print(card)