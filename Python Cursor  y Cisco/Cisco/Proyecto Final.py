import random

# Valores iniciales del tablero
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9


def display_board(A, B, C, D, E, F, G, H, I):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(A) + "   |   " + str(B) + "   |   " + str(C) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(D) + "   |   " + str(E) + "   |   " + str(F) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(G) + "   |   " + str(H) + "   |   " + str(I) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def check_winner(A, B, C, D, E, F, G, H, I, symbol):
    if A == symbol and B == symbol and C == symbol:
        return True
    if D == symbol and E == symbol and F == symbol:
        return True
    if G == symbol and H == symbol and I == symbol:
        return True

    if A == symbol and D == symbol and G == symbol:
        return True
    if B == symbol and E == symbol and H == symbol:
        return True
    if C == symbol and F == symbol and I == symbol:
        return True

    if A == symbol and E == symbol and I == symbol:
        return True
    if C == symbol and E == symbol and G == symbol:
        return True

    return False


def board_full(A, B, C, D, E, F, G, H, I):
    if A != "X" and A != "O":
        return False
    if B != "X" and B != "O":
        return False
    if C != "X" and C != "O":
        return False
    if D != "X" and D != "O":
        return False
    if E != "X" and E != "O":
        return False
    if F != "X" and F != "O":
        return False
    if G != "X" and G != "O":
        return False
    if H != "X" and H != "O":
        return False
    if I != "X" and I != "O":
        return False

    return True


# ==============================
# TURNO 1: Máquina siempre centro
# ==============================
E = "X"

while True:

    # Mostrar tablero
    display_board(A, B, C, D, E, F, G, H, I)

    # Verificar si la máquina ya ganó
    if check_winner(A, B, C, D, E, F, G, H, I, "X"):
        print("La máquina gana.")
        break

    # Verificar empate
    if board_full(A, B, C, D, E, F, G, H, I):
        print("Empate.")
        break

    # ==============================
    # TURNO DEL USUARIO (O)
    # ==============================
    x = int(input("Ingresa un movimiento (1/9): "))

    if x == 1 and A != "X" and A != "O":
        A = "O"
    elif x == 2 and B != "X" and B != "O":
        B = "O"
    elif x == 3 and C != "X" and C != "O":
        C = "O"
    elif x == 4 and D != "X" and D != "O":
        D = "O"
    elif x == 5 and E != "X" and E != "O":
        E = "O"
    elif x == 6 and F != "X" and F != "O":
        F = "O"
    elif x == 7 and G != "X" and G != "O":
        G = "O"
    elif x == 8 and H != "X" and H != "O":
        H = "O"
    elif x == 9 and I != "X" and I != "O":
        I = "O"
    else:
        print("Movimiento inválido o casilla ocupada.")
        continue

    # Verificar si el usuario ganó
    if check_winner(A, B, C, D, E, F, G, H, I, "O"):
        display_board(A, B, C, D, E, F, G, H, I)
        print("Tú ganas.")
        break

    # Verificar empate
    if board_full(A, B, C, D, E, F, G, H, I):
        display_board(A, B, C, D, E, F, G, H, I)
        print("Empate.")
        break

    # ==============================
    # TURNO DE LA MÁQUINA (X random)
    # ==============================
    while True:
        pc_move = random.randint(1, 9)

        if pc_move == 1 and A != "X" and A != "O":
            A = "X"
            break
        elif pc_move == 2 and B != "X" and B != "O":
            B = "X"
            break
        elif pc_move == 3 and C != "X" and C != "O":
            C = "X"
            break
        elif pc_move == 4 and D != "X" and D != "O":
            D = "X"
            break
        elif pc_move == 5 and E != "X" and E != "O":
            E = "X"
            break
        elif pc_move == 6 and F != "X" and F != "O":
            F = "X"
            break
        elif pc_move == 7 and G != "X" and G != "O":
            G = "X"
            break
        elif pc_move == 8 and H != "X" and H != "O":
            H = "X"
            break
        elif pc_move == 9 and I != "X" and I != "O":
            I = "X"
            break
