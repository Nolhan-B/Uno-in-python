import random
from time import sleep

from engine.Cards.basic.NumberCard import NumberCard
from engine.GameConfig import GameConfig
from engine.Player import Player
from engine.constants import GameStatus
from engine.deck import Deck
from engine.exceptions import (
    NotEnoughPlayersError,
    TooManyPlayersError, GameNotReadyError, InvalidCardIndexError, CardNotPlayableError
)
from engine.rules import Rules


class GameEngine:
    def __init__(self, game_config: GameConfig) -> None:
        self.status = GameStatus.PREPARING
        self.deck = Deck()
        self.players = []
        self.discard_pile = []
        self.current_player_index = 0
        self.direction = 1
        self.game_config = game_config

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def prepare_game(self) -> None:
        if len(self.players) < 2:
            raise NotEnoughPlayersError("Need at least 2 players")
        if len(self.players) > 4:
            raise TooManyPlayersError("Max 4 players")

        self.deck.shuffle()
        for _ in range(self.game_config.cards_per_player):
            for player in self.players:
                player.hand.add_card(self.deck.draw())

        self.current_player_index = random.randint(0, len(self.players) - 1)

        print("=" * 40)
        print(f"\nStarted game with {len(self.players)} players")
        print(f"Player '{self.players[self.current_player_index].name}' will begin\n")
        print("=" * 40)

        while not isinstance(self.deck.preview_next_card(), NumberCard):
            self.deck.shuffle()

        self.discard_pile.append(self.deck.draw())
        self.status = GameStatus.RTP

    def _get_card_nb_from_user(self) -> int:
        player_asked = self.get_current_player()
        while True:
            try:
                value = int(input("Card number to play: "))
                if value > len(player_asked.hand.cards) or value < 0:
                    raise InvalidCardIndexError("Invalid card number")
                if not Rules.is_card_playable(
                        player_asked.hand.cards[value],
                        self.discard_pile[-1]
                ):
                    raise CardNotPlayableError("You cannot play this card.")
                break
            except (ValueError, IndexError, EOFError):
                print("Invalid card number")
            except (InvalidCardIndexError, CardNotPlayableError) as e:
                print(e)
        return int(value)

    # def _play_card_for_user(self, index: int) -> None:


    def run(self) -> None:
        if self.status != GameStatus.RTP:
            raise GameNotReadyError("Game hasn't been prepared yet.")

        self.status = GameStatus.PLAYING

        while self.status == GameStatus.PLAYING:
            for player in self.players:
                print(player.name, "hand:", end=" ")
                for i, card in enumerate(player.hand.cards):
                    print(f"[{i}]", "playable" if Rules.is_card_playable(card, self.discard_pile[-1]) else "not playable", card, end=" | ")
                print("\n")
                print("=" * 20, "\n")
            print(f"Last card is: {self.discard_pile[-1]}")
            card_to_play = self._get_card_nb_from_user()
            break

    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]