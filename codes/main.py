class Game:
    def __init__(self):
        self.running = False
        rows = 8
        self.board = []
        for _ in range(rows):
            self.board.append([" " for _ in range(8)])

        self.setup_board()
        


    def setup_board(self):

        

        self.board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
        self.board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]
        self.board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
        self.board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]

    def move(self):
        y_start = int(input("Y Start: "))
        x_start = int(input("X Start: "))
        y_end = int(input("Y End: "))
        X_end = int(input("X End: "))
        
        self.board[y_end][X_end] = self.board[y_start][x_start] 
        self.board[y_start][x_start] = " "

        print(self.board[x_start][y_end]) 



    def draw_board(self):
        for cell in self.board:
            print(cell)

    def run(self):
        self.running = True
        while self.running:
            self.draw_board()
            self.move()


g = Game()
g.run()