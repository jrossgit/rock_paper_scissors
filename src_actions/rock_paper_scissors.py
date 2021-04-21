from enum import Enum

from src_actions.game import Game


class WinStateEnum(Enum):
    LOSS = -1
    UNKNOWN = 0
    DRAW = 1
    WIN = 2


class RockPaperScissorsPlayerState(Game):

    def __init__(self):
        self.move = None
        self.result = WinStateEnum.UNKNOWN

    def serialized(self, see_private=True):
        if see_private or not self.move:
            return {"selected_move": self.move}
        else:
            return {"selected_move": "unknown"}


class RockPaperScissorsGame(Game):

    min_players = 2
    max_players = 2

    def _intialise_game_state(self):
        self.moves_revealed = False
        for player in self.players:
            player.set_state(RockPaperScissorsPlayerState())

    def take_action(self, player, action, **params):

        if action == "choose_move":
            self.get_player(player).state.move = params["move"]

            if all([p.state.move for p in self.players]):
                self.moves_revealed = True

                p1, p2 = [p.state for p in self.players]
                if p1.move == p2.move:
                    p1.result = p2.result = WinStateEnum.DRAW
                elif (
                        (p1.move == "rock" and p2.move == "scissors") or
                        (p1.move == "paper" and p2.move == "rock") or
                        (p1.move == "scissors" and p2.move == "paper")):
                    p1.result = WinStateEnum.WIN
                    p2.result = WinStateEnum.LOSS
                elif (
                        (p1.move == "rock" and p2.move == "paper") or
                        (p1.move == "paper" and p2.move == "scissors") or
                        (p1.move == "scissors" and p2.move == "rock")):
                    p1.result = WinStateEnum.LOSS
                    p2.result = WinStateEnum.WIN

    def _check_progress(self):
        return all([p.state.move for p in self.players])

    def serialized(self, player):

        players = []
        for p in self.players:
            data = {
                "name": p.name,
                "you": p.name == player,
                "win": p.state.result.name,
            }
            print(self.moves_revealed)
            if (p.name == player) or self.moves_revealed:
                data.update(p.state.serialized(see_private=True))
            else:
                data.update(p.state.serialized(see_private=False))
            players.append(data)
        return {
            "players": players
        }
