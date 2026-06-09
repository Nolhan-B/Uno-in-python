from engine.hand import Hand


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = Hand()
