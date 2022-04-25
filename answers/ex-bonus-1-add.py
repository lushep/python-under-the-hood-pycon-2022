class Deck:
   
    def __len__(self):
        return len(self._cards)
        
    def __str__(self):
        return f'Deck(suits={self.suits}, ranks={self.ranks})'
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __add__(self, other):
        return self._cards + other._cards
    
    def deal(self):
        return self._cards.pop()
    
    def check_ace(self):
        return self.cards[-1].rank == 'A'

class AvatarDeck(Deck):
    ranks = list('23456789T') + ['Sokka', 'Katara', 'Zuko', 'Aang']
    suits = ['Water', 'Air', 'Fire', 'Water']
    
    def __init__(self):
        Card = collections.namedtuple('Card', ['rank', 'suit'])
        self._cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
        
class French52Deck(Deck):
    ranks = '23456789TJQKA'
    suits = '♠♥♦♣'
    
    def __init__(self):
        Card = collections.namedtuple('Card', ['rank', 'suit'])
        self._cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]

avatar_deck = AvatarDeck()
deck = French52Deck()

both = deck + avatar_deck
len(both)