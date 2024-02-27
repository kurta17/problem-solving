def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = 0
    
    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists.")
        return False
    
    print("Solution exists. Here's the board:")
    for row in board:
        print(row)

    return True


n = int(input())
solve_n_queens(n)
