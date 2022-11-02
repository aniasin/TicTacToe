

class Player:
    def __init__(self, checker, avatar):
        self.avatar = avatar
        self.checker = checker

    def player_action(self):
        correct_input = False
        player_move = ""
        while not correct_input:
            player_move = input("Enter the coordinates of your move as 'xy': ")
            valid_choices = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
            try:
                int(player_move)
                correct_input = player_move in valid_choices
            except (ValueError, TypeError):
                pass

            if not correct_input:
                print("Could not interpret input.")

        self.checker.set_box_content(int(player_move[1]), int(player_move[0]), self.avatar)


class Robot(Player):
    def player_action(self):
        correct_input = False
        while not correct_input:
            if self.checker.set_box_content(1, 1, self.avatar):
                break
            correct_input = self.find_move()

    def find_move(self):
        for j in range(0, 3):
            line = [self.checker.array[j][i].content for i in range(0, 3)]
            if line.count("X") > 1:
                for i in range(0, 3):
                    if self.checker.set_box_content(j, i, self.avatar):
                        return True
            if line.count(self.avatar) > 1:
                for i in range(0, 3):
                    if self.checker.set_box_content(j, i, self.avatar):
                        return True
        index = 0
        for row in self.checker.array:
            for i in range(0, 3):
                if self.checker.set_box_content(index, i, self.avatar):
                    return True
            index += 1
        return False
