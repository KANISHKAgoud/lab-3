N = 8 

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):

    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == N:
        print("Final 8-Queens Matrix:")
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1 
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  

    return False

board = [[0]*N for _ in range(N)]
board[0][0] = 1 

print("Initial Board (First Queen Placed):")
print_board(board)
solve_n_queens(board, 1)

