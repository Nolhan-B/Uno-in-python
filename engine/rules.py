from engine.Cards.Card import Card
from engine.Cards.basic.DrawTwoCard import DrawTwoCard
from engine.Cards.basic.NumberCard import NumberCard
from engine.Cards.basic.ReverseCard import ReverseCard
from engine.Cards.basic.SkipCard import SkipCard
from engine.Cards.basic.WildCard import WildCard
from engine.Cards.basic.WildDrawFourCard import WildDrawFourCard


class Rules:
    @staticmethod
    def is_card_playable(card: Card, top_card: Card) -> bool:
        match card:
            case WildCard() | WildDrawFourCard():
                return True
            case NumberCard():
                assert isinstance(top_card, NumberCard)
                return card.color == top_card.color or card.number == top_card.number
            case SkipCard() | ReverseCard() | DrawTwoCard() :
                return card.color == top_card.color or type(card) == type(top_card)
            case _:
                return False