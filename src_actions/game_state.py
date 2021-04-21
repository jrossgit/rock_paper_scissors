from enum import Enum


class WinStateEnum(Enum):
    LOSS = -1
    UNKNOWN = 0
    DRAW = 1
    WIN = 2


class ChoiceEnum(Enum):
    NOT_CHOSEN = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Player:

    def __init__(self, name: str):
        self.name: str = name
        self.choice: ChoiceEnum =


# class RockPaperScissorsGame:

#     def