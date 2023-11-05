import os
logo =  ("▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄\n"
"█       █       █       █       █\n"
"█   ▄▄▄▄█   ▄   █▄     ▄█   ▄   █\n"
"█  █  ▄▄█  █▄█  █ █   █ █  █ █  █\n"
"█  █ █  █       █ █   █ █  █▄█  █\n"
"█  █▄▄█ █   ▄   █ █   █ █       █\n"
"█▄▄▄▄▄▄▄█▄▄█ █▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█")


def print_board(board):
    for item in board:
        print(f"|  {item[0]}  |  {item[1]}  |  {item[2]}  |")
        print("-------------------")


def check_board(board) -> bool:
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            return True

    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True
    return False


board_map = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

print(logo)
print("\t\tBienvenidos!\n\t\tInstrucciones:\nEl jugador 1 sera identificado con O y el jugador 2 con X")
print("El tablero es el siguiente:")
print_board(board_map)
print("Durante el turno de cada, el jugador debera ingresar un numero disponible dentro del tablero para"
      "crear una marca")
print("Cuando algun jugador logre hilar tres marcas sera el ganador. Si al llenarse el tablero nadie resulto"
      "ganador, el encuentro termina en empate")

start = input("Presiona algun boton para empezar: ")
game_on = True
jugador = 1
mensaje = ""
jugadas = 0
while game_on:
    os.system('clear')
    print(mensaje)
    if jugador == 1:
        player = 1

    else:
        player = 2
    print(f"Jugador {player}")

    print_board(board_map)
    indice = int(input("Ingrese la localizacion de su pieza: "))

    # Test whether or not the place is already taken
    fila = 0
    columna = 0
    if 10 > indice > 0:
        if indice - 7 >= 0:
            fila = 2
            columna = indice - 7
        elif indice - 4 >= 0:
            fila = 1
            columna = indice - 4
        else:
            fila = 0
            columna = indice - 1
    else:
        mensaje = "Numero fuera del tablero. Intente de nuevo"
        continue

    if board_map[fila][columna] != "X" and board_map[fila][columna] != "O":
        if jugador == 1:
            board_map[fila][columna] = "O"
        else:
            board_map[fila][columna] = "X"
        jugador = jugador * -1
        jugadas += 1
        mensaje = ""


    #Checamos las condiciones del juego
    # Se completo una fila
    if check_board(board_map):
        print_board(board_map)
        print(f"El jugador {player} ha ganado!")
        game_on = False
        continue
    # Esta lleno el tablero
    if jugadas == 9:
        #os.system('clear')
        print("\t\tEMPATE")
        game_on = False
        continue
















