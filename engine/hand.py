from typing import List

from engine.Cards.Card import Card


class Hand:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards or []
