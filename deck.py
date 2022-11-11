class Card:
    """Represents a standard playing card"""

    suit_icon = ["\u2663", "\u2666", "\u2665", "\u2660"]
    suit_name = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_name = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, icon, rank):
        self.icon = icon
        self.suit = icon
        self.rank = rank

    def __str__(self):
        return "%s of %s %s" % (Card.rank_name[self.rank], Card.suit_name[self.suit], Card.suit_icon[self.icon])


class Deck:
    def __init__(self):
        self.cards = []
        for icon in range(4):
            for rank in range(1, 14):
                card = Card(icon, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
