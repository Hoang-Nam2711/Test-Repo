"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks={}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >=2:
                return True
        return False

    def has_twopair(self):
        self.rank_hist()
        i=0
        for val in self.ranks.values():
            if val >=2:
                i+=1
        if i>=2:
            return True
        return False
    
    def has_threekind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val>=3:
                return True
        return False

    def has_straight(self):
        ranks=self.ranks.copy()
        ranks[14]=ranks.get(1,0) #Condition: 10-Jack-Queen-King-Ace
        count=0
        for i in range (1,15):
            if ranks.get(i,0): 
                #If hand has the next rank ranks.get(i,0) return the number so it's true, else return 0 so it's false
                count+=1
                if count == 5:
                    return True
            else:
                count=0
        return False

    def has_fullhouse(self):
        self.rank_hist()
        count=0
        i=2
        for val in self.ranks.values():
            if val==i:
                count+=1
                i+=1
        if count>=2:
            return True
        return False 
    
    def has_fourkind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val>=4:
                return True
        return False
    
    def has_straightflush(self):
        s=set()
        for c in self.cards:
            s.add((c.rank,c.suit))
            if c.rank==1:
                s.add((14,c.suit))
        for suit in range (4):
            count=0
            for rank in range (1,15):
                if (suit,rank) in s:
                    count+=1
                    if count==5:
                        return True
                count=0
        return False
    
    def test_Repo():
        pass

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(5):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print("Flush?:",hand.has_flush())
        print("Pair?:", hand.has_pair())
        print("Two Pair?:", hand.has_twopair())
        print("Has Threekind?", hand.has_threekind())
        print("Straight?:", hand.has_straight())
        print("Full House?:", hand.has_fullhouse())
        print("Four Kind?:", hand.has_fourkind())
        print("Straight Flush?", hand.has_straightflush())
        print('')

