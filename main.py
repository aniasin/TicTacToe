from checker import Checker
from player import Player, Robot

checker = Checker()
player = Player(checker, "X")
robot = Robot(checker, "O")

is_game_over = len(checker.winners) > 0
while not is_game_over:
    player.player_action()
    robot.player_action()


