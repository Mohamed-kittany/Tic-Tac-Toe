from tic_tac_toe import TicTacToe


def get_valid_name():
    while True:
        # Remove any leading/trailing whitespace
        name = input("Enter your name: ").strip()

        # Check if the name contains only letters and spaces
        if name and all(char.isalpha() or char.isspace() for char in name):
            return name # Return the valid name
        print("Invalid name. Please use only letters and spaces.")


def replay_game():
    while True:
        # Prompt the user to decide if they want to play another game
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        print("Invalid input. Please type 'yes' or 'no'.")


def main():
    print("Welcome to 3-D Triple-Decker Tic-Tac-Toe!")
    # Get valid names for the two players
    player1 = get_valid_name()
    player2 = get_valid_name()

    # Initialize scores for both players
    scores = {player1: 0, player2: 0}

    while True:
        # Create a new game instance with the players and their scores
        tic_tac_toe = TicTacToe([player1, player2], scores)
        # Start the game
        tic_tac_toe.play()

        # Check if players want to replay after the game ends
        if not replay_game():
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
