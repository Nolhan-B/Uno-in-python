from engine.Cards.Card import Card
from engine.constants import CardColor


class ReverseCard(Card):
    def __init__(self, color: CardColor) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return f"{self.color.value} reverse"

    def apply_effects(self, game_engine: "GameEngine") -> None:
        print("test")