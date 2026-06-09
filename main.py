from engine.GameConfig import GameConfig
from engine.GameEngine import GameEngine
from engine.Player import Player


def main() -> None:
    config = GameConfig()
    engine = GameEngine(config)
    engine.add_player(Player("player1"))
    engine.add_player(Player("player2"))

    engine.prepare_game()
    engine.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("unhandled exception :", e)
