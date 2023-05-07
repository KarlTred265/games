from random import randint

# set up game boards
player_board = []
computer_board = []
for x in range(0, 5):
    player_board.append(["O"] * 5)
    computer_board.append(["O"] * 5)

# place battleships on computer board
def place_battleships(board):
    for i in range(5):
        ship_row = randint(0, len(board) - 1)
        ship_col = randint(0, len(board[0]) - 1)
        board[ship_row][ship_col] = "B"
        
# print board function
def print_board(board):
    for row in board:
        print(" ".join(row))

# initial placement of battleships on computer board
place_battleships(computer_board)

# main game loop
num_guesses = 0
num_battleships = 5
playing = True

while playing:
    # print player board
    print("Player board:")
    print_board(player_board)
    
    # get user guess
    guess_row = input("Guess Row (A-E): ")
    guess_col = input("Guess Col (1-5): ")
    
    # validate guess input
    valid_input = False
    while not valid_input:
        if guess_row.upper() in ['A', 'B', 'C', 'D', 'E'] and guess_col in ['1', '2', '3', '4', '5']:
            valid_input = True
        else:
            print("Invalid input. Please enter a letter A-E and a number 1-5.")
            guess_row = input("Guess Row (A-E): ")
            guess_col = input("Guess Col (1-5): ")
            
    # convert guess to board coordinates
    row = ord(guess_row.upper()) - 65
    col = int(guess_col) - 1
    
    # check if user has already guessed that coordinate
    if player_board[row][col] == "X":
        print("You already guessed that coordinate!")
        continue
    
    # check if user guessed a battleship
    if computer_board[row][col] == "B":
        print("Congratulations! You sunk a battleship!")
        computer_board[row][col] = "X"
        num_battleships -= 1
        player_board[row][col] = "X"
    else:
        print("You missed!")
        player_board[row][col] = "X"
    
    # check if user won
    if num_battleships == 0:
        print("Congratulations! You sunk all the battleships!")
        playing = False
    else:
        num_guesses += 1
        
        # check if user has any guesses left
        if num_guesses == 10:
            print("Game over! You ran out of guesses.")
            playing = False
    
    # print computer board
    print("\nComputer board:")
    computer_board_display = []
    for i in range(len(computer_board)):
        computer_board_display.append([])
        for j in range(len(computer_board[0])):
            if computer_board[i][j] == "B":
                computer_board_display[i].append("O")
            else:
                computer_board_display[i].append(computer_board[i][j])
    print_board(computer_board_display)
    
# ask user if they want to play again
play_again = input("Do you want to play again? (y/n) ")
while play_again.lower() not in ['y', 'n']:
    play_again = input("Invalid input. Please enter 'y' for")