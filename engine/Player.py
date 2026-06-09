import uuid

from engine.hand import Hand


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = str(uuid.uuid4())
        self.hand = Hand([])
