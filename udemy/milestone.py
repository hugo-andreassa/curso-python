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
    player1 = ""
    player2 = ""

    while player1 != "X" and player1 != "O":
        player1 = input("Please pick a marker 'X' or 'O': ")

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker

    return board


# display_board(['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'])
# player = player_input()
# print(player)

test_board = place_marker(['#', '', '', '', 'O', '', '', 'X', 'O', ''], 'X', 3)
display_board(test_board)

