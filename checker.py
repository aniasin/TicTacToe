import numpy as np


class CheckerBox:
    def __init__(self, content):
        self.content = content
        self.visual_1 = " _____ "
        self.visual_2 = "|     |"
        self.visual_3 = f"|  {content}  |"
        self.visual_4 = "|_____|"
        self.lines = [self.visual_1, self.visual_2, self.visual_3, self.visual_4]

    def get_line(self, line):
        return self.lines[line]

    def set_content(self, content):
        self.content = content


class Checker:
    def __init__(self):
        self.array = np.array([[CheckerBox(" "), CheckerBox(" "), CheckerBox(" ")],
                              [CheckerBox(" "), CheckerBox(" "), CheckerBox(" ")],
                              [CheckerBox(" "), CheckerBox(" "), CheckerBox(" ")]])
        self.title = "      T̳I̳C̳ T̳A̳C̳ T̳O̳E̳"
        self.visualize()
        self.winners = []

    def visualize(self):
        print(self.title)
        index = 0
        for row in self.array:
            for line in range(0, 4):
                if line == 2:
                    coord = str(index)
                else:
                    coord = " "
                line = coord + row[0].get_line(line) + row[1].get_line(line) + row[2].get_line(line)
                print(line)
            index += 1
        print("    0      1      2")

    def set_box_content(self, x, y, content):
        is_possible = self.array[x][y].content == " "
        if is_possible:
            self.array[x][y] = CheckerBox(content)
            self.visualize()

        self.check_winner()
        if len(self.winners) > 0:
            return True
        return is_possible

    def check_winner(self):
        all_symbols = []
        for row in range(0, 3):
            line = [self.array[row][i].content for i in range(0, 3)]
            all_symbols += (self.array[row][i].content for i in range(0, 3))
            if line.count("X") == 3:
                self.winners = ["You"]
                return
            if line.count("O") == 3:
                self.winners = ["Robot"]
                return

        if " " not in all_symbols:
            self.winners = ["You", "Robot"]
            return

        for column in range(0, 3):
            line = [self.array[i][column].content for i in range(0, 3)]
            if line.count("X") == 3:
                self.winners = ["You"]
                return
            if line.count("O") == 3:
                self.winners = ["Robot"]
                return

        line = []
        for index in range(0, 3):
            line.append(self.array[index][index].content)
        if line.count("X") == 3:
            self.winners = ["You"]
            return
        if line.count("O") == 3:
            self.winners = ["Robot"]
            return
        index_2 = 2
        line = []
        for index in range(0, 3):
            line.append(self.array[index][index_2].content)
            index_2 -= 1
        if line.count("X") == 3:
            self.winners = ["You"]
            return
        if line.count("O") == 3:
            self.winners = ["Robot"]
            return

    def get_winner(self):
        if len(self.winners) > 1:
            return "It's a draw."
        return self.winners[0]
