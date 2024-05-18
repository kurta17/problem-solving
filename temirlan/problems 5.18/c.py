n = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if j < i:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-i]


for i in dp:
    print(i)

print(dp[n][n] - 1)