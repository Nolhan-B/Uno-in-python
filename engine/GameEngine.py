from engine.GameConfig import GameConfig
from engine.Player import Player
from engine.deck import Deck
from engine.exceptions import (
    NotEnoughPlayersError,
    TooManyPlayersError
)


class GameEngine:
    def __init__(self, game_config: GameConfig) -> None:
        self.deck = Deck()
        self.players = []
        self.discard_pile = []
        self.current_player_index = 0
        self.direction = 1
        self.game_config = game_config

    def add_player(self, player: Player) -> None:
        self.players.append(player)
        print(f"Added player '{player.name}'")

    def start_game(self) -> None:
        if len(self.players) < 2:
            raise NotEnoughPlayersError("Need at least 2 players")
        if len(self.players) > 4:
            raise TooManyPlayersError("Max 4 players")
