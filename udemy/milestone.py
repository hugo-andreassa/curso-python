from random import randrange


def display_board(board):
    print('{0:^8} | {1:^8} | {2:^8}'.format("", "", ""))
    print('{0:^8} | {1:^8} | {2:^8}'.format(board[7], board[8], board[9]))
    print('{0:^8} | {1:^8} | {2:^8}'.format("", "", ""))

    print('{0:^8} | {1:^8} | {2:^8}'.format("-------", "-------", "-------"))
    print('{0:^8} | {1:^8} | {2:^8}'.format("", "", ""))
    print('{0:^8} | {1:^8} | {2:^8}'.format(board[6], board[5], board[4]))
    print('{0:^8} | {1:^8} | {2:^8}'.format("", "", ""))
    print('{0:^8} | {1:^8} | {2:^8}'.format("-------", "-------", "-------"))

    print('{0:^8} | {1:^8} | {2:^8}'.format("", "", ""))
    print('{0:^8} | {1:^8} | {2:^8}'.format(board[3], board[2], board[1]))
    print('{0:^8} | {1:^8} | {2:^8}'.format("", "", ""))


def player_input():
    player = ""
    player2 = ""

    while player != "X" and player != "O":
        player = input("Please pick a marker 'X' or 'O': ")

    if player == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player, player2


def place_marker(board, marker, position):
    board[position] = marker

    return board


def verifica_vencedor(board, marker):
    pass


# Primeiro escolhe o jogador
jogada_inicio = randrange(1, 3)
player1 = ''
player2 = ''
ganhador = ''
board_game = ['#', '', '', '', '', '', '', '', '', '']

if jogada_inicio == 1:
    print("Jogador 1 começa!")
    players = player_input()

    player1 = players[0]
    player2 = players[1]
else:
    print("Jogador 2 começa!")
    players = player_input()

    player2 = players[0]
    player1 = players[1]

while ganhador != 0:
    pass

# Depois faz a jogada
# Mostra o quadro

# Depois o outro jogador faz a jogada
# Mostra o quadro

# ...

# Verifica quem ganhou ou se deu empate

# Pergunta se quer jogar dnv

# display_board()


player1 = ''
# players[0]


test_board = place_marker(['#', '', '', '', 'O', '', '', 'X', 'O', ''], 'X', 3)
display_board(test_board)
