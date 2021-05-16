from .game_state import ChoiceEnum, WinStateEnum


def update_win_states(game):

    if (game.players[0].state.move == ChoiceEnum.NOT_CHOSEN or
            game.players[1].state.move == ChoiceEnum.NOT_CHOSEN):
        return

    c1 = game.players[0].state.move
    c2 = game.players[1].state.move
    if (c1 == ChoiceEnum.ROCK and c2 == ChoiceEnum.ROCK or
            c1 == ChoiceEnum.PAPER and c2 == ChoiceEnum.PAPER or
            c1 == ChoiceEnum.SCISSORS and c2 == ChoiceEnum.SCISSORS):
        game.players[0].state.win_state = WinStateEnum.DRAW
        game.players[1].state.win_state = WinStateEnum.DRAW
    elif (c1 == ChoiceEnum.ROCK and c2 == ChoiceEnum.SCISSORS or
            c1 == ChoiceEnum.PAPER and c2 == ChoiceEnum.ROCK or
            c1 == ChoiceEnum.SCISSORS and c2 == ChoiceEnum.PAPER):
        game.players[0].state.win_state = WinStateEnum.WIN
        game.players[1].state.win_state = WinStateEnum.LOSS
    else:
        game.players[0].state.win_state = WinStateEnum.LOSS
        game.players[1].state.win_state = WinStateEnum.WIN


def player_choice(game, player_name: str, action: ChoiceEnum):

    player = game.player(player_name)
    player.state.move = action
    update_win_states(game)
