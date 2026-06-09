import random
from time import sleep

from engine.GameConfig import GameConfig
from engine.Player import Player
from engine.constants import GameStatus
from engine.deck import Deck
from engine.exceptions import (
    NotEnoughPlayersError,
    TooManyPlayersError, GameNotReadyError
)


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

        self.discard_pile.append(self.deck.draw())

        self.status = GameStatus.RTP

    def run(self) -> None:
        if self.status != GameStatus.RTP:
            raise GameNotReadyError("Game hasn't been prepared yet.")

        self.status = GameStatus.PLAYING

        while self.status == GameStatus.PLAYING:
            sleep(2)
            break
