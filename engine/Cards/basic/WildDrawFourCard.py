from engine.Cards.Card import Card
from engine.GameEngine import GameEngine
from engine.constants import CardColor


class WildDrawFourCard(Card):
    def __init__(self) -> None:
        super().__init__(CardColor.WILD)

    def __str__(self) -> str:
        return "Draw Four Wild Card"

    def apply_effects(self, game_engine: "GameEngine") -> None:
        print("test")
