from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.GameEngine import GameEngine
from engine.Cards.Card import Card
from engine.constants import CardColor


class DrawTwoCard(Card):
    def __init__(self, color: CardColor) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return f"{self.color.value} Draw Two"

    def apply_effects(self, game_engine: "GameEngine") -> None:
        print("test")
