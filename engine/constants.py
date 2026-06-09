from enum import Enum


class CardColor(Enum):
    YELLOW = "yellow"
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    WILD = "wild"


class GameStatus(Enum):
    PREPARING = "Preparing"
    RTP = "Ready To Play"
    PLAYING = "Playing"
    FINISHED = "Finished"