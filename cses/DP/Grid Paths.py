n = int(input())

grid = [input() for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 0 if grid[0][0] == '*' else 1
for i in range(n):
    for j in range(n):
        if grid[i][j] == '.':
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1000000007

# print(dp[0])
# print(dp[1])
# print(dp[2])
# print(dp[3])
print(dp[-1][-1])