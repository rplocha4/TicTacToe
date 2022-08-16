from tkinter import *
from tkinter import messagebox

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
X_COLOR = '#2ab7ca'
O_COLOR = '#7bc043'
WINNING_LINE_COLOR = '#d11141'
BORDER_COLOR = '#fff'
X_WIDTH = 25
O_WIDTH = 25
WINNING_LINE_WIDTH = 25
LINE_WIDTH = 10


class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.iconbitmap('icon.ico')
        self.window.title("Tic Tac Toe")
        self.canvas = Canvas(self.window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
        self.canvas.pack()

        self.computer = 'O'
        self.player = 'X'
        self.turn = self.player
        self.message = ''
        self.game_over = False

        self.print_lines()

        self.area1 = [0, 0, CANVAS_HEIGHT / 3, CANVAS_WIDTH / 3, False, None]
        self.area2 = [CANVAS_HEIGHT / 3, 0, 2 * (CANVAS_HEIGHT / 3), CANVAS_WIDTH / 3, False, None]
        self.area3 = [2 * (CANVAS_HEIGHT / 3), 0, CANVAS_HEIGHT, CANVAS_WIDTH / 3, False, None]
        self.area4 = [0, CANVAS_WIDTH / 3, CANVAS_HEIGHT / 3, 2 * (CANVAS_WIDTH / 3), False, None]
        self.area5 = [CANVAS_HEIGHT / 3, CANVAS_WIDTH / 3, 2 * (CANVAS_HEIGHT / 3), 2 * (CANVAS_WIDTH / 3), False, None]
        self.area6 = [2 * (CANVAS_HEIGHT / 3), CANVAS_WIDTH / 3, CANVAS_HEIGHT, 2 * (CANVAS_WIDTH / 3), False, None]
        self.area7 = [0, 2 * (CANVAS_WIDTH / 3), CANVAS_HEIGHT / 3, CANVAS_WIDTH, False, None]
        self.area8 = [CANVAS_HEIGHT / 3, 2 * (CANVAS_WIDTH / 3), 2 * (CANVAS_HEIGHT / 3), CANVAS_WIDTH, False, None]
        self.area9 = [2 * (CANVAS_HEIGHT / 3), 2 * (CANVAS_WIDTH / 3), CANVAS_HEIGHT, CANVAS_WIDTH, False, None]

        self.areas = [self.area1, self.area2, self.area3, self.area4, self.area5, self.area6, self.area7, self.area8,
                      self.area9]

        self.canvas.bind("<Button-1>", self.player_move)

        self.canvas.pack()

    def mainloop(self):
        self.window.mainloop()

    def player_move(self, event):
        y = int(CANVAS_HEIGHT / 3)
        x = int(CANVAS_WIDTH / 3)
        if not x - LINE_WIDTH / 2 <= event.x <= x + LINE_WIDTH / 2 \
                and not x * 2 - LINE_WIDTH / 2 <= event.x <= x * 2 + LINE_WIDTH / 2 \
                and not y - LINE_WIDTH / 2 <= event.y <= y + LINE_WIDTH / 2 \
                and not y * 2 - LINE_WIDTH / 2 <= event.y <= y * 2 + LINE_WIDTH / 2:
            for area in self.areas:
                if area[0] < event.x < area[2] and area[1] < event.y < area[3]:
                    x1, y1, x2, y2 = area[0], area[1], area[2], area[3]
                    if not area[4]:
                        self.draw_x(x1, y1, x2, y2)
                        area[5] = self.player
                        area[4] = True

                        if self.check_for_win():
                            self.mark_win("PLAYER")

                        elif self.check_for_draw():
                            self.mark_draw()

                        else:
                            self.computer_move()
                    break

        if self.game_over:
            if messagebox.askquestion(self.message, "Next Game?") == 'yes':
                self.reset_game()

    def print_lines(self):
        y = int(CANVAS_HEIGHT / 3)
        x = int(CANVAS_WIDTH / 3)
        self.canvas.create_line(0, y, CANVAS_WIDTH, y, fill=BORDER_COLOR, width=LINE_WIDTH)
        self.canvas.create_line(0, y * 2, CANVAS_WIDTH, y * 2, fill=BORDER_COLOR, width=LINE_WIDTH)

        self.canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill=BORDER_COLOR, width=LINE_WIDTH)
        self.canvas.create_line(x * 2, 0, x * 2, CANVAS_HEIGHT, fill=BORDER_COLOR, width=LINE_WIDTH)

    def draw_o(self, x, y, x2, y2):
        self.canvas.create_oval(x + O_WIDTH, y + O_WIDTH, x2 - O_WIDTH, y2 - O_WIDTH, width=O_WIDTH, outline=O_COLOR)

    def draw_x(self, x, y, x2, y2):
        self.canvas.create_line(x + X_WIDTH, y + X_WIDTH, x2 - X_WIDTH, y2 - X_WIDTH, width=X_WIDTH, fill=X_COLOR,
                                capstyle="round")
        self.canvas.create_line(x + X_WIDTH, y2 - X_WIDTH, x2 - X_WIDTH, y + X_WIDTH, width=X_WIDTH, fill=X_COLOR,
                                capstyle="round")

    def draw_winning_line(self, x, y, x1, y1):
        self.canvas.create_line(x, y, x1, y1, width=WINNING_LINE_WIDTH, fill=WINNING_LINE_COLOR, capstyle="round")

    def check_for_win(self):
        if self.areas[0][5] == self.areas[1][5] == self.areas[2][5] and self.areas[0][5] is not None:
            self.draw_winning_line(0, CANVAS_WIDTH / 6, CANVAS_WIDTH, CANVAS_WIDTH / 6)
            return True
        if self.areas[3][5] == self.areas[4][5] == self.areas[5][5] and self.areas[3][5] is not None:
            self.draw_winning_line(0, CANVAS_WIDTH / 2, CANVAS_WIDTH, CANVAS_WIDTH / 2)
            return True
        if self.areas[6][5] == self.areas[7][5] == self.areas[8][5] and self.areas[6][5] is not None:
            self.draw_winning_line(0, CANVAS_WIDTH / 1.2, CANVAS_WIDTH, CANVAS_WIDTH / 1.2)
            return True
        if self.areas[0][5] == self.areas[3][5] == self.areas[6][5] and self.areas[0][5] is not None:
            self.draw_winning_line(CANVAS_HEIGHT / 6, 0, CANVAS_HEIGHT / 6, CANVAS_HEIGHT)
            return True
        if self.areas[1][5] == self.areas[4][5] == self.areas[7][5] and self.areas[1][5] is not None:
            self.draw_winning_line(CANVAS_HEIGHT / 2, 0, CANVAS_HEIGHT / 2, CANVAS_HEIGHT)
            return True
        if self.areas[2][5] == self.areas[5][5] == self.areas[8][5] and self.areas[2][5] is not None:
            self.draw_winning_line(CANVAS_HEIGHT / 1.2, 0, CANVAS_HEIGHT / 1.2, CANVAS_HEIGHT)
            return True
        if self.areas[2][5] == self.areas[4][5] == self.areas[6][5] and self.areas[2][5] is not None:
            self.draw_winning_line(CANVAS_WIDTH, 0, 0, CANVAS_HEIGHT)
            return True
        if self.areas[0][5] == self.areas[4][5] == self.areas[8][5] and self.areas[0][5] is not None:
            self.draw_winning_line(self.areas[0][0], self.areas[0][1], self.areas[8][2], self.areas[8][3])
            return True

    def mark_win(self, winner):
        self.message = f'{winner} WON'
        self.game_over = True
        self.canvas.unbind("<Button-1>")

    def check_for_draw(self):
        for area in self.areas:
            if area[5] is None:
                return False
        return True

    def mark_draw(self):
        self.message = 'DRAW'
        self.game_over = True
        self.canvas.unbind("<Button-1>")

    def reset_game(self):
        self.game_over = False
        for area in self.areas:
            area[4], area[5] = False, None
        self.canvas.delete("all")
        self.turn = 'O'
        self.print_lines()
        self.canvas.bind("<Button-1>", self.player_move)

    def evaluate(self):
        if self.areas[0][5] == self.areas[1][5] == self.areas[2][5] and self.areas[0][5] is not None:
            if self.areas[0][5] == self.computer:
                return 10
            return -10
        if self.areas[3][5] == self.areas[4][5] == self.areas[5][5] and self.areas[3][5] is not None:
            if self.areas[3][5] == self.computer:
                return 10
            return -10
        if self.areas[6][5] == self.areas[7][5] == self.areas[8][5] and self.areas[6][5] is not None:
            if self.areas[6][5] == self.computer:
                return 10
            return -10
        if self.areas[0][5] == self.areas[3][5] == self.areas[6][5] and self.areas[0][5] is not None:
            if self.areas[0][5] == self.computer:
                return 10
            return -10
        if self.areas[1][5] == self.areas[4][5] == self.areas[7][5] and self.areas[1][5] is not None:
            if self.areas[1][5] == self.computer:
                return 10
            return -10
        if self.areas[2][5] == self.areas[5][5] == self.areas[8][5] and self.areas[2][5] is not None:
            if self.areas[2][5] == self.computer:
                return 10
            return -10
        if self.areas[2][5] == self.areas[4][5] == self.areas[6][5] and self.areas[2][5] is not None:
            if self.areas[2][5] == self.computer:
                return 10
            return -10
        if self.areas[0][5] == self.areas[4][5] == self.areas[8][5] and self.areas[0][5] is not None:
            if self.areas[0][5] == self.computer:
                return 10
            return -10
        return 0

    def find_best_move(self):
        best_value = -1
        best_move = None

        for area in self.areas:
            if area[5] is None:
                area[5] = self.computer
                move_value = self.minimax(0, False)
                area[5] = None
                if move_value > best_value:
                    best_value = move_value

                    best_move = area

        return best_move

    def minimax(self, depth, is_maximizer):
        score = self.evaluate()

        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if self.check_for_draw():
            return 0

        if is_maximizer:
            best_value = -1000
            for area in self.areas:
                if area[5] is None:
                    area[5] = self.computer
                    best_value = max(best_value, self.minimax(depth + 1, not is_maximizer))
                    area[5] = None
        else:
            best_value = 1000
            for area in self.areas:
                if area[5] is None:
                    area[5] = self.player
                    best_value = min(best_value, self.minimax(depth + 1, not is_maximizer))
                    area[5] = None

        return best_value

    def computer_move(self):
        best_move = self.find_best_move()
        best_move[5] = self.turn
        x1, y1, x2, y2 = best_move[0], best_move[1], best_move[2], best_move[3]
        self.draw_o(x1, y1, x2, y2)
        best_move[5] = self.computer

        best_move[4] = True
        if self.check_for_win():
            self.mark_win("COMPUTER")
        if self.check_for_draw() and not self.game_over:
            self.mark_draw()


if __name__ == "__main__":
    game = TicTacToe()

    game.mainloop()
