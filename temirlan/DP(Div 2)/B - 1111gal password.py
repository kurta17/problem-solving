n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(1,10):
        if j == 1:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % 998244353
        elif j == 9:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 998244353
        else:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]) % 998244353
        
         
print(sum(dp[n]) % 998244353)