import random


class TicTacToe:
    def __init__(self, players, scores):
        # Create a 3x3x3 board
        self.board = [[["-" for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.players = players
        # Randomly select which player starts the game.
        self.current_player = 0 if random.choice([True, False]) else 1
        self.game_over = False
        self.symbols = ['X', 'O']
        self.scores = scores

    # Print the current state of the board.
    def print_board(self):
        print("\n")
        for level in range(3):
            print(f"Level {level + 1}")
            for row in range(3):
                print(" | ".join(self.board[level][row]))
            print("\n")

    # Display which player's turn it is.
    def print_player_turn(self):
        print(f"It's {self.players[self.current_player]}'s turn ({self.symbols[self.current_player]})")

    # Display which player's turn it is.
    def switch_player(self):
        self.current_player = 1 - self.current_player

    # Handle player moves input.
    def get_move(self):
        valid = False
        while not valid:
            move_input = input(f"{self.players[self.current_player]}, enter your move (level, row, col): ")
            try:
                level, row, col = map(int, move_input.split())
                # Validate the coordinates are within bounds.
                if 0 <= level < 3 and 0 <= row < 3 and 0 <= col < 3:
                    if self.board[level][row][col] == "-":
                        self.board[level][row][col] = self.symbols[self.current_player]
                        return True
                    else:
                        print("That spot is already taken. Please choose another.")
                else:
                    print("Invalid move. Levels, rows, and columns must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter three numbers separated by spaces.")
        return False

    # Check if there's a winner.
    def check_winner(self):
        board = self.board

        # Check vertical lines in each level for each column
        for level in range(3):
            for col in range(3):
                if board[level][0][col] == board[level][1][col] == board[level][2][col] != "-":
                    return True

        # Check diagonal from top left to bottom right in each level
        for level in range(3):
            if board[level][0][0] == board[level][1][1] == board[level][2][2] != "-":
                return True

        # Check vertical lines across levels for each position
        for row in range(3):
            for col in range(3):
                if board[0][row][col] == board[1][row][col] == board[2][row][col] != "-":
                    return True

        # Check diagonal across levels from one corner to opposite
        if board[0][0][0] == board[1][1][1] == board[2][2][2] != "-":
            return True
        if board[0][2][0] == board[1][1][1] == board[2][0][2] != "-":
            return True

        # Check horizontal lines in each row for each level
        for level in range(3):
            for row in range(3):
                if board[level][row][0] == board[level][row][1] == board[level][row][2] != "-":
                    return True

        # Check diagonal lines for depth in each column
        for col in range(3):
            if board[0][0][col] == board[1][1][col] == board[2][2][col] != "-":
                return True
            if board[0][2][col] == board[1][1][col] == board[2][0][col] != "-":
                return True

        # Check vertical lines in each column within each level
        for level in range(3):
            for col in range(3):
                if board[level][0][col] == board[level][1][col] == board[level][2][col] != "-":
                    return True

        return False  # No winner found

    # Update the score for the winning player.
    def update_scores(self, winner):
        self.scores[winner] += 1

    # Display the scores of all players.
    def print_scores(self):
        print("Current Scores:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")

    # Main game loop.
    def play(self):
        while not self.game_over:
            self.print_board()
            self.print_player_turn()

            if not self.get_move():
                self.switch_player()

            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Congratulations {self.players[self.current_player]}! You won!")
                self.update_scores(self.players[self.current_player])
                self.print_scores()
                self.game_over = True
            elif all(cell != '-' for level in self.board for row in level for cell in row):
                self.print_board()
                print("The game is a tie!")
                self.game_over = True
            else:
                self.switch_player()
