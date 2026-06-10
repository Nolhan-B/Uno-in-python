import random
from typing import List

from engine.Cards.Card import Card
from engine.Cards.basic.DrawTwoCard import DrawTwoCard
from engine.Cards.basic.NumberCard import NumberCard
from engine.Cards.basic.ReverseCard import ReverseCard
from engine.Cards.basic.SkipCard import SkipCard
from engine.Cards.basic.WildCard import WildCard
from engine.Cards.basic.WildDrawFourCard import WildDrawFourCard
from engine.constants import CardColor


class Deck:
    def __init__(self,
                 qty_numbers=2,
                 qty_skip=2,
                 qty_reverse=2,
                 qty_draw_two=2,
                 qty_wild=4,
                 qty_wild_draw_four=4
                 ) -> None:
        self.qty_numbers = qty_numbers
        self.qty_skip = qty_skip
        self.qty_reverse = qty_reverse
        self.qty_draw_two = qty_draw_two
        self.qty_wild = qty_wild
        self.qty_wild_draw_four = qty_wild_draw_four
        self.cards: List[Card] = self._generate_cards()

    def _generate_cards(self) -> List[Card]:
        cards = []
        for color in [CardColor.RED,
                      CardColor.GREEN,
                      CardColor.BLUE,
                      CardColor.YELLOW]:
            cards.append(NumberCard(color, 0))
            for number in range(1, 10):
                for _ in range(self.qty_numbers):
                    cards.append(NumberCard(color, number))
            for _ in range(self.qty_skip):
                cards.append(SkipCard(color))
            for _ in range(self.qty_reverse):
                cards.append(ReverseCard(color))
            for _ in range(self.qty_draw_two):
                cards.append(DrawTwoCard(color))
        for _ in range(self.qty_wild):
            cards.append(WildCard())
        for _ in range(self.qty_wild_draw_four):
            cards.append(WildDrawFourCard())
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def preview_next_card(self) -> Card | None:
        return self.cards[-1] if self.cards else None

    def draw(self) -> Card:
        return self.cards.pop()
