def is_end_reachable(board: str) -> bool:
    n = len(board)
    dp = [[False, False] for _ in range(n)]
    dp[0][0] = dp[0][1] = True

    for i in range(1, n):
        if board[i] == 'X':
            continue
        for j in range(2):
            if i - 1 >= 0 and dp[i - 1][j]:
                dp[i][j] = True
            if i - 3 >= 0 and dp[i - 3][j]:
                dp[i][j] = True
            if j == 1 and i - 5 >= 0 and dp[i - 5][0]:
                dp[i][1] = True

    return dp[n- 1][1]

# assert is_end_reachable("oXooXXXXXoo") == True

print(is_end_reachable("oXooXXXXoo"))

