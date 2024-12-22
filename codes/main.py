
class Piece:
    def __init__(self, color="white"):
        self.color = color

    def validate_move(self):
        pass

    def move(self):
        pass


class Pawn(Piece):
    def __init__(self, color="white"):
        super().__init__(color)

    def __repr__(self):
        return "P" if self.color == "white" else "p"

class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.board = []
        self.setup_board()


    def setup_board(self):
        for _ in range(self.rows):
            self.board.append([" " for _ in range(self.cols)])

        self.board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
        self.board[1] = [Pawn("b") for _ in range(self.cols)]
        self.board[6] = [Pawn() for _ in range(self.cols)]
        self.board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        


    def print_board(self):
        for cell in self.board:
            print(cell)

