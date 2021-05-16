from enum import Enum


class WinStateEnum(Enum):
    LOSS = -1
    UNKNOWN = 0
    DRAW = 1
    WIN = 2


class ChoiceEnum(Enum):
    HIDDEN = -1
    NOT_CHOSEN = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Player:

    def __init__(self, name, state=None):
        self.name = name
        self.state = state

    def serialized(self, requester):

        is_you: bool = requester == self.name

        return {
            "name": self.name,
            "you": is_you,
            "state": self.state.serialized(see_private=is_you),
        }


class RockPaperScissorsPlayerState:

    def __init__(self, move=ChoiceEnum.NOT_CHOSEN):
        self.move = move
        self.result = WinStateEnum.UNKNOWN

        self.win_state = WinStateEnum.UNKNOWN

    def serialized(self, see_private):
        if see_private or not self.move:
            return {
                "selected_move": self.move,
                "win_state": self.win_state,
            }
        else:
            return {
                "selected_move": ChoiceEnum.HIDDEN,
                "win_state": self.win_state,
            }


class RockPaperScissorsGame:

    min_players = 2
    max_players = 2

    def __init__(self, players):
        self.players = players

    def player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def serialized(self, player):

        players = []
        for p in self.players:
            data = {
                "name": p.name,
                "you": p.name == player,
                "win_state": p.state.result.name,
            }

            if (p.name == player) or self.moves_revealed:
                data.update(p.state.serialized(see_private=True))
            else:
                data.update(p.state.serialized(see_private=False))
            players.append(data)
        return {
            "players": players
        }
