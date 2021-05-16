from unittest import TestCase

from .actions import player_choice
from .game_state import (
    ChoiceEnum,
    Player,
    RockPaperScissorsGame,
    RockPaperScissorsPlayerState,
    WinStateEnum,
)

class TestSerialization(TestCase):

    def setUp(self):

        self.players = [
            Player(
                name="Jay",
                state=RockPaperScissorsPlayerState(
                    move=ChoiceEnum.PAPER
                )
            ),
            Player(
                name="Kay",
                state=RockPaperScissorsPlayerState(
                    move=ChoiceEnum.NOT_CHOSEN
                )
            )
        ]
        self.game = RockPaperScissorsGame(
            players=self.players
        )

    def test_player_public_serialization(self):

        player1 = self.players[0].serialized(requester="Jay")
        assert player1["name"] == "Jay"
        assert player1["you"] == True
        assert player1["state"]["selected_move"] == ChoiceEnum.PAPER
        assert player1["state"]["win_state"] == WinStateEnum.UNKNOWN

    def test_player_secret_serialization(self):

        player1 = self.players[0].serialized(requester="Kay")
        assert player1["name"] == "Jay"
        assert player1["you"] == False
        assert player1["state"]["selected_move"] == ChoiceEnum.HIDDEN
        assert player1["state"]["win_state"] == WinStateEnum.UNKNOWN


class TestActions(TestCase):

    def setUp(self):

        self.players = [
            Player(
                name="Jay",
                state=RockPaperScissorsPlayerState(
                    move=ChoiceEnum.PAPER
                )
            ),
            Player(
                name="Kay",
                state=RockPaperScissorsPlayerState(
                    move=ChoiceEnum.NOT_CHOSEN
                )
            )
        ]
        self.game = RockPaperScissorsGame(
            players=self.players
        )

    def test_player_choosing_action_changes_action(self):

        player_choice(self.game, "Jay", ChoiceEnum.ROCK)
        assert self.players[0].state.move == ChoiceEnum.ROCK
        assert self.players[1].state.move == ChoiceEnum.NOT_CHOSEN

        player_choice(self.game, "Kay", ChoiceEnum.PAPER)
        assert self.players[0].state.move == ChoiceEnum.ROCK
        assert self.players[1].state.move == ChoiceEnum.PAPER

    def test_player_choosing_action_changes_win_state(self):
        player_choice(self.game, "Jay", ChoiceEnum.ROCK)
        assert self.players[0].state.win_state == WinStateEnum.UNKNOWN
        assert self.players[1].state.win_state == WinStateEnum.UNKNOWN

        player_choice(self.game, "Kay", ChoiceEnum.PAPER)
        assert self.players[0].state.win_state == WinStateEnum.LOSS
        assert self.players[1].state.win_state == WinStateEnum.WIN
