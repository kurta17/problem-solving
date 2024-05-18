n, m = map(int, input().split())
x = list(map(int, input().split()))

dp = [[0] * (m + 2) for _ in range(n + 1)]
mod = 10**9 + 7

for i in range(1, n + 1):
    if x[i-1] == 0:
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % mod
    else:
        if i == 1:
            dp[i][x[i-1]] = 1
        else:
            dp[i][x[i-1]] = (dp[i-1][x[i-1]-1] + dp[i-1][x[i-1]] + dp[i-1][x[i-1]+1]) % mod

print(sum(dp[-1]) % mod)