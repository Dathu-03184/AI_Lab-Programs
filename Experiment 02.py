N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row):
    if row == N:
        print_board(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)

def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Start
board = [-1] * N
solve(board, 0)
