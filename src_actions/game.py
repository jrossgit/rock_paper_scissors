from enum import Enum


class GameStateEnum(Enum):
    CREATED = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class Game:

    min_players = None
    max_players = None

    def __init__(self):
        if self.min_players is None or self.max_players is None:
            raise NotImplementedError("Game class must define min/max players")

    def start_game(self, players):
        if len(players) > self.max_players or len(players) < self.min_players:
            raise RuntimeError("Wrong number of players")
        self.players = players
        self._intialise_game_state()

    def _intialise_game_state(self):
        raise NotImplementedError("Implement game state initialiser")

    def take_action(self, player, action, **params):
        raise NotImplementedError("Implement actions")

    def get_player(self, name):
        for p in self.players:
            if p.name == name:
                return p

    def _check_progress(self):
        raise NotImplementedError("Implement game progress check")


class Player:

    def __init__(self, name):
        self.name = name
        self.state = None

    def set_state(self, state):
        self.state = state


class GameLifecycle:

    def __init__(self, game_class):
        self.state = GameStateEnum.CREATED
        self.game = game_class()
        self.players = []

    def add_player(self, name):
        self.players.append(Player(name))

    def start_game(self):
        self.state = GameStateEnum.IN_PROGRESS
        self.game.start_game(self.players)

    def take_action(self, player, action, **params):
        self.game.take_action(player, action, **params)
        if self.game._check_progress():
            self.state = GameStateEnum.COMPLETE

    def serialized(self, player_name):
        return {
            "game_status": str(self.state.name),
            "game": self.game.serialized(player_name)
        }
