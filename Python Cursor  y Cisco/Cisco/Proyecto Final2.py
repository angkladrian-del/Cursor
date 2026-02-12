
from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print("|   " + str(board[row][0]) + "   |   " + str(board[row][1]) + "   |   " + str(board[row][2]) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        move = input("Ingresa tu movimiento (1-9): ")

        if move.isdigit() == False:
            print("Error: debes ingresar un número.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Error: el número debe estar entre 1 y 9.")
            continue

        # Buscar la casilla dentro del tablero
        for row in range(3):
            for col in range(3):
                if board[row][col] == move:
                    board[row][col] = "O"
                    return

        print("Casilla ocupada, elige otra.")


def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                free.append((row, col))

    return free


def victory_for(board, sign):
    # Filas
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    # Columnas
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    # Diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


def draw_move(board):
    free = make_list_of_free_fields(board)

    if len(free) == 0:
        return

    move_index = randrange(len(free))
    row, col = free[move_index]

    board[row][col] = "X"


# ==============================
# Programa principal
# ==============================

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# La máquina siempre empieza en el centro
board[1][1] = "X"

while True:

    display_board(board)

    if victory_for(board, "X"):
        print("La máquina gana.")
        break

    if len(make_list_of_free_fields(board)) == 0:
        print("Empate.")
        break

    enter_move(board)

    if victory_for(board, "O"):
        display_board(board)
        print("Tú ganas.")
        break

    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Empate.")
        break

    draw_move(board)

from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print("|   " + str(board[row][0]) + "   |   " + str(board[row][1]) + "   |   " + str(board[row][2]) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        move = input("Ingresa tu movimiento (1-9): ")

        if move.isdigit() == False:
            print("Error: debes ingresar un número.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Error: el número debe estar entre 1 y 9.")
            continue

        # Buscar la casilla dentro del tablero
        for row in range(3):
            for col in range(3):
                if board[row][col] == move:
                    board[row][col] = "O"
                    return

        print("Casilla ocupada, elige otra.")


def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                free.append((row, col))

    return free


def victory_for(board, sign):
    # Filas
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    # Columnas
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    # Diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


def draw_move(board):
    free = make_list_of_free_fields(board)

    if len(free) == 0:
        return

    move_index = randrange(len(free))
    row, col = free[move_index]

    board[row][col] = "X"


# ==============================
# Programa principal
# ==============================

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# La máquina siempre empieza en el centro
board[1][1] = "X"

while True:

    display_board(board)

    if victory_for(board, "X"):
        print("La máquina gana.")
        break

    if len(make_list_of_free_fields(board)) == 0:
        print("Empate.")
        break

    enter_move(board)

    if victory_for(board, "O"):
        display_board(board)
        print("Tú ganas.")
        break

    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Empate.")
        break

    draw_move(board)

