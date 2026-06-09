from engine.Cards.Card import Card
from engine.constants import CardColor


class NumberCard(Card):
    def __init__(self, color: CardColor, number: int) -> None:
        super().__init__(color)
        self.number = number

    def __str__(self) -> str:
        return f"{self.color.value} {self.number}"

    def apply_effects(self, game_engine: "GameEngine") -> None:
        print("test")