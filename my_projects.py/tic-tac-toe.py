import os

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_details():
    print(f"{BOLD}{CYAN}\n=== Tic-Tac-Toe Game Details ==={RESET}")
    print(f"{YELLOW}How to Play:{RESET}")
    print("- The game is played on a 3x3 grid.")
    print("- Players take turns to place their symbol (X or O) in an empty spot.")
    print("- The first player to get 3 of their symbols in a row (vertically, horizontally, or diagonally) wins.")
    print("- If all 9 spots are filled and no player has 3 in a row, the game ends in a draw.\n")
    print(f"{MAGENTA}Position guide:{RESET}")
    print(f" {BOLD}1{RESET} | {BOLD}2{RESET} | {BOLD}3{RESET} ")
    print("---+---+---")
    print(f" {BOLD}4{RESET} | {BOLD}5{RESET} | {BOLD}6{RESET} ")
    print("---+---+---")
    print(f" {BOLD}7{RESET} | {BOLD}8{RESET} | {BOLD}9{RESET} \n")

def colored_symbol(symbol):
    if symbol == "X":
        return f"{RED}{BOLD}X{RESET}"
    elif symbol == "O":
        return f"{GREEN}{BOLD}O{RESET}"
    else:
        return " "

def display_board(board):
    print()
    print(f" {colored_symbol(board[0])} | {colored_symbol(board[1])} | {colored_symbol(board[2])} ")
    print("---+---+---")
    print(f" {colored_symbol(board[3])} | {colored_symbol(board[4])} | {colored_symbol(board[5])} ")
    print("---+---+---")
    print(f" {colored_symbol(board[6])} | {colored_symbol(board[7])} | {colored_symbol(board[8])} ")
    print()

def player_move(board, player):
    while True:
        try:
            move = int(input(f"{CYAN}Player {colored_symbol(player)} - Enter your move (1-9): {RESET}")) - 1
            if move < 0 or move > 8:
                print(f"{YELLOW}Invalid move! Choose a number between 1 and 9.{RESET}")
            elif board[move] != " ":
                print(f"{YELLOW}That spot is already taken. Try again.{RESET}")
            else:
                board[move] = player
                break
        except ValueError:
            print(f"{YELLOW}Invalid input! Enter a number only.{RESET}")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return " " not in board

def play_game():
    board = [" "] * 9
    current_player = "X"

    clear_screen()
    print(f"{BOLD}{MAGENTA}🎮 Welcome to Tic-Tac-Toe (2 Player Mode) 🎮{RESET}")
    show_details()

    while True:
        display_board(board)
        player_move(board, current_player)

        clear_screen()
        print(f"{BOLD}{MAGENTA}🎮 Tic-Tac-Toe (2 Player Mode) 🎮{RESET}")
        show_details()

        if check_winner(board, current_player):
            display_board(board)
            print(f"{GREEN}{BOLD}🎉 Player {colored_symbol(current_player)} wins! 🎉{RESET}")
            break
        elif is_draw(board):
            display_board(board)
            print(f"{CYAN}{BOLD}🤝 It's a draw!{RESET}")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()