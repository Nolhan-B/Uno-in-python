from engine.Cards.Card import Card
from engine.GameEngine import GameEngine
from engine.constants import CardColor


class SkipCard(Card):
    def __init__(self, color: CardColor) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return f"{self.color.value} Skip"

    def apply_effects(self, game_engine: "GameEngine") -> None:
        print("test")
