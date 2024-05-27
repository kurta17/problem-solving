n = int(input())


dp = [[0] * 3 for _ in range(n+1)]
dp[1][0] = 3
dp[1][1] = 1
dp[1][2] = 0

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] * 3 + dp[i-1][1] * 3 + dp[i-1][2] * 3
    dp[i][1] = dp[i-1][0]
    dp[i][2] = dp[i-1][1]


ans = dp[n][0] + dp[n][1] + dp[n][2]
print(ans)