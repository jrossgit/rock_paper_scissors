from src.game import GameLifecycle
from src.rock_paper_scissors import RockPaperScissorsGame


def test_rock_paper_scissors():
    game_manager = GameLifecycle(RockPaperScissorsGame)
    game_manager.add_player("Jay")
    game_manager.add_player("Kay")
    game_manager.start_game()
    game_manager.take_action("Jay", "choose_move", move="rock")

    assert game_manager.serialized("Jay")["game_status"] == "IN_PROGRESS"
    assert game_manager.serialized("Jay")["game"]["players"] == [
            {
                "name": "Jay",
                "you": True,
                "selected_move": "rock",
                "win": "UNKNOWN"
            },
            {
                "name": "Kay",
                "you": False,
                "selected_move": None,
                "win": "UNKNOWN"
            }
        ]
    assert game_manager.serialized("Kay")["game"]["players"] == [
            {
                "name": "Jay",
                "you": False,
                "selected_move": "unknown",
                "win": "UNKNOWN"
            },
            {
                "name": "Kay",
                "you": True,
                "selected_move": None,
                "win": "UNKNOWN"
            }
        ]

    game_manager.take_action("Kay", "choose_move", move="scissors")
    assert game_manager.serialized("Jay")["game"]["players"] == [
        {
            "name": "Jay",
            "you": True,
            "selected_move": "rock",
            "win": "WIN"
        },
        {
            "name": "Kay",
            "you": False,
            "selected_move": "scissors",
            "win": "LOSS"
        }
    ]
    assert game_manager.serialized("Jay")["game_status"] == "COMPLETE"