from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.GameEngine import GameEngine
from engine.Cards.Card import Card
from engine.constants import CardColor


class WildCard(Card):
    def __init__(self) -> None:
        super().__init__(CardColor.WILD)

    def __str__(self) -> str:
        return "Wild Card"

    def apply_effects(self, game_engine: "GameEngine") -> None:
        print("test")
