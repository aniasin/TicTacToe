from checker import Checker
from player import Player, Robot
import random

player_start = False
player_score = 0
robot_score = 0


def start_game(is_first_game):
    global player_start
    global player_score
    global robot_score
    checker = Checker()
    player = Player(checker, "X")
    robot = Robot(checker, "O")
    if is_first_game:
        if random.randint(0, 100) < 51:
            player_start = True
    else:
        player_start = not player_start

    while len(checker.winners) == 0:
        if player_start:
            player.player_action()
            if len(checker.winners) == 0:
                robot.player_action()
        else:
            robot.player_action()
            if len(checker.winners) == 0:
                player.player_action()

        print(len(checker.winners))

    winner = checker.get_winner()
    if winner == "You":
        player_score += 1
    elif winner == "Robot":
        robot_score += 1
    if winner == f"It's a draw.":
        print(f"{winner} Your score : {player_score} - Robot's score : {robot_score}")
    else:
        print(f"Victory for {winner}  Your score : {player_score} - Robot's score : {robot_score}")
    if player.play_again():
        start_game(False)


start_game(True)
