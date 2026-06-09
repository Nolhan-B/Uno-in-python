from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.GameEngine import GameEngine

from engine.constants import CardColor
from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, color: CardColor) -> None:
        self.color = color

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def apply_effects(self, game_engine: "GameEngine") -> None:
        pass
