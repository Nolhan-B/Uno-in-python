from typing import List

from engine.Cards.Card import Card


class Hand:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards or []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)