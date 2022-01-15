import random

suits = ( 'Hearts', 'Diamonds', 'Spades', 'Clubs')
card_names = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def __str__(self):
    return f'{self.value} of {self.suit}'


class Deck:
  def __init__(self):
    self.deck = []
    self.dealt = []
    for suit in suits:
      for card in card_names:
        self.deck.append(Card(suit, card))

  def __str__(self):
    return f'{[value for value in self.deck if print(value)]}'

  def deal(self):
    single_card = self.deck.pop(random.randrange(len(self.deck)))
    self.dealt.append(single_card)
    return single_card


if __name__ == "__main__":
  deck = Deck()
  # print(deck)
  player1card1 = deck.deal()
  player1card2 = deck.deal()
  player2card1 = deck.deal()
  player2card2 = deck.deal()
  player3card1 = deck.deal()
  player3card2 = deck.deal()
  dealercard1 = deck.deal()
  dealercard2 = deck.deal()    
  
  for i, card in enumerate(deck.dealt):
    if i %2 == 0:
      print('')
    print(card)

