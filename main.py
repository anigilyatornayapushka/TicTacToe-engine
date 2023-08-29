import random


E = 0
X = 1
O = 2

GAME = 0
X_W = 1
O_W = 2
TIE = 3

tictactoe = [
    [E,E,E],
    [E,E,E],
    [E,E,E],
]


def print_board():
    f = ['.', 'x', 'o']
    print(
        '\n    1   2   3\n'
        '  +---+---+---+\n'
        f'a | {f[tictactoe[0][0]]} | {f[tictactoe[0][1]]} | {f[tictactoe[0][2]]} | a\n'
        '  +---+---+---+\n'
        f'b | {f[tictactoe[1][0]]} | {f[tictactoe[1][1]]} | {f[tictactoe[1][2]]} | b\n'
        '  +---+---+---+\n'
        f'c | {f[tictactoe[2][0]]} | {f[tictactoe[2][1]]} | {f[tictactoe[2][2]]} | c\n'
        '  +---+---+---+\n'
        '    1   2   3\n\n'
    )


def is_end():
    for i in range(3):
        if tictactoe[0][i] == tictactoe[1][i] == tictactoe[2][i]:
            if tictactoe[0][i] == X:
                return X_W
            elif tictactoe[0][i] == O:
                return O_W

        if tictactoe[i][0] == tictactoe[i][1] == tictactoe[i][2]:
            if tictactoe[i][0] == X:
                return X_W
            elif tictactoe[i][0] == O:
                return O_W

    if tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2]:
        if tictactoe[1][1] == X:
            return X_W
        elif tictactoe[1][1] == O:
            return O_W

    if tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0]:
        if tictactoe[1][1] == X:
            return X_W
        elif tictactoe[1][1] == O:
            return O_W

    if E not in tictactoe[0] and E not in tictactoe[1] and E not in tictactoe[2]:
        return TIE

    return GAME


def end_game(result):
    print(['', 'X Win', 'O Win', 'Tie'][result])


def do_move_real(symb):
    coords = {'a': 0, 'b': 1, 'c': 2, '1': 0, '2': 1, '3': 2}
    move = input('Your move: ')

    if move[0] not in coords or move[1] not in coords:
        return do_move_real(symb)

    a = coords[move[0]]
    b = coords[move[1]]

    if tictactoe[a][b]:
        return do_move_real(symb)

    tictactoe[a][b] = symb


def do_move_engine(symb):

    def find_result(ssymb):
        result = is_end()
        if result != GAME:
            if result == symb:
                return (2,)
            if result == TIE:
                return (1,)
            return (0,)

        all_results = []
        for y in range(3):
            for x in range(3):
                if tictactoe[y][x] != E:
                    continue
                tictactoe[y][x] = ssymb
                res = find_result(3-ssymb)
                all_results.append((res[0], y, x))
                tictactoe[y][x] = E

        all_results.sort(key=lambda x: x[0], reverse=symb!=ssymb)
        return all_results[-1]

    _, y, x = find_result(symb)
    tictactoe[y][x] = symb


def main():
    player1 = random.randrange(1,3)
    player2 = 3 - player1
    move = 1

    while True:
        print_board()

        if result := is_end():
            return end_game(result)

        if player1 & move:
            do_move_real(player1)
        else:
            do_move_engine(player2)

        move = 3 - move


if __name__ == '__main__':
    main()
