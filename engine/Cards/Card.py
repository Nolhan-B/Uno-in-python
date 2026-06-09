from abc import ABC, abstractmethod

from engine.constants import CardColor

class Card(ABC):
    def __init__(self, color: CardColor) -> None:
        self.color = color

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def apply_effects(self, game_engine: "GameEngine") -> None:
        pass
