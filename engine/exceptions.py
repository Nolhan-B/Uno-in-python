class NotEnoughPlayersError(Exception):
    pass


class TooManyPlayersError(Exception):
    pass


class GameNotReadyError(Exception):
    pass

class InvalidCardIndexError(Exception):
    pass

class CardNotPlayableError(Exception):
    pass