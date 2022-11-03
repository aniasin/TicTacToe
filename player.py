

class Player:
    def __init__(self, checker, avatar):
        self.avatar = avatar
        self.checker = checker
        self.other_avatar = ""
        if self.avatar == "X":
            self.other_avatar = "O"
        else:
            self.other_avatar = "X"

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

    def play_again(self):
        correct_input = False
        while not correct_input:
            response = input("Wanna play again ? 'y', 'n' : ")
            valid_choices = ["y", "n"]

            correct_input = response in valid_choices
            if not correct_input:
                print("Could not interpret input.")
        return response == 'y'


class Robot(Player):
    def player_action(self):
        correct_input = False
        while not correct_input:
            if self.checker.set_box_content(1, 1, self.avatar):
                break
            correct_input = self.find_move()

    def find_move(self):
        # Check each row if there is two 'X' or 'O'
        line = []
        for row in range(0, 3):
            line = [self.checker.array[row][i].content for i in range(0, 3)]
            if line.count(self.avatar) == 2:
                for i in range(0, 3):
                    if self.checker.set_box_content(row, i, self.avatar):
                        return True
            if line.count(self.other_avatar) == 2:
                for i in range(0, 3):
                    if self.checker.set_box_content(row, i, self.avatar):
                        return True

        # Check each column
        for column in range(0, 3):
            line = [self.checker.array[i][column].content for i in range(0, 3)]
            if line.count(self.avatar) == 2:
                for i in range(0, 3):
                    if self.checker.set_box_content(i, column, self.avatar):
                        return True
            if line.count(self.other_avatar) == 2:
                for i in range(0, 3):
                    if self.checker.set_box_content(i, column, self.avatar):
                        return True

        # Check diagonals
        line = []
        for index in range(0, 3):
            line.append(self.checker.array[index][index].content)
        if line.count(self.other_avatar) == 2:
            for index in range(0, 3):
                if self.checker.set_box_content(index, index, self.avatar):
                    return True
        if line.count(self.avatar) == 2:
            for index in range(0, 3):
                if self.checker.set_box_content(index, index, self.avatar):
                    return True
        index_2 = 2
        line = []
        for index in range(0, 3):
            line.append(self.checker.array[index][index_2].content)
            index_2 -= 1

        if line.count(self.other_avatar) == 2:
            index_2 = 2
            for index in range(0, 3):
                if self.checker.set_box_content(index, index_2, self.avatar):
                    return True
                index_2 -= 1
        if line.count(self.avatar) == 2:
            index_2 = 2
            for index in range(0, 3):
                if self.checker.set_box_content(index, index_2, self.avatar):
                    return True
                index_2 -= 1

        # First action found if center is occupied
        if self.checker.set_box_content(1, 1, self.avatar):
            return True
        index = 0
        for row in self.checker.array:
            for i in range(0, 3):
                if self.checker.set_box_content(index, i, self.avatar):
                    return True
            index += 1
        return False
