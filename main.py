import sys
def freopen(filename, mode):
    if mode == "r":
        sys.stdin = open(filename, mode)
    elif mode == "w":
        sys.stdout = open(filename, mode)


def string_check(first_chess_board, second_chess_board, figure, count, result):
    if first_chess_board[figure] != count:
        if first_chess_board[figure] + second_chess_board[figure] < count:
            return False
        for i in range(count - first_chess_board[figure]):
            result.append(figure)
    return True

# ---- MAIN ----
freopen("chess.in", "r")
freopen("chess.out", "w")

def main():
    full_chess_board = {
     'black king':1,
     'black queen':1,
     'black rook':2,
     'black bishop':2,
     'black knight':2,
     'black pawn': 8,
     'white king':1,
     'white queen':1,
     'white rook':2,
     'white bishop':2,
     'white knight':2,
     'white pawn': 8,
    }


    first_chess_board = {
     'black king':0,
     'black queen':0,
     'black rook':0,
     'black bishop':0,
     'black knight':0,
     'black pawn': 0,
     'white king':0,
     'white queen':0,
     'white rook':0,
     'white bishop':0,
     'white knight':0,
     'white pawn': 0,
    }
    result = []
    counts = str(input()).split(' ')
    first_board_count, second_board_count = int(counts[0]), int(counts[1])
    second_chess_board = first_chess_board.copy()

    for i in range(first_board_count):
        first_chess_board[str(input())] += 1

    for i in range(second_board_count):
        second_chess_board[str(input())] += 1

    for k, v in full_chess_board.items():
        if (False == string_check(first_chess_board, second_chess_board, k, v, result)):
            return "impossible\n"
        
    return '\n'.join(result)

print(main())