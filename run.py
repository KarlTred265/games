import random

def generate_board(size):
    board = []
    for row in range(size):
        board.append(["O"] * size)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_ships(num_ships, board):
    ships = []
    for i in range(num_ships):
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        while [ship_row, ship_col] in ships:
            ship_row = random.randint(0, len(board) - 1)
            ship_col = random.randint(0, len(board[0]) - 1)
        ships.append([ship_row, ship_col])
    return ships

def play_game(size, num_ships):
    board = generate_board(size)
    ships = generate_ships(num_ships, board)
    print("Welcome to Battleships!")
    print(f"You have {num_ships} ships to sink.")
    print(f"Board size: {size}x{size}")
    print_board(board)
    for turn in range(10):
        guess_row = int(input("Guess row (0 to {}): ".format(size - 1)))
        guess_col = int(input("Guess col (0 to {}): ".format(size - 1)))
        if [guess_row, guess_col] in ships:
            print("Congratulations! You sank a battleship!")
            board[guess_row][guess_col] = "X"
            ships.remove([guess_row, guess_col])
        else:
            if guess_row not in range(size) or \
                guess_col not in range(size):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
        print(f"Turn {turn + 1}:")
        print_board(board)
        if not ships:
            print("Congratulations! You sank all the battleships!")
            break
    else:
        print("Game over! You ran out of turns.")
        print(f"The remaining battleships were at:")
        for ship in ships:
            print(f"({ship[0]}, {ship[1]})")

def replay_game():
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        play_game(size, num_ships)
    else:
        print("Thanks for playing!")

size = 10
num_ships = 5
play_game(size, num_ships)
replay_game()