n = int(input())


dp = [[0 for i in range(9)] for j in range(n+1)]
dp[2][:] = [3]*8 + [2]

for i in range(2,n+1):
    for j in range(n+1):
        dp[i][j] = dp[i-1][j] 
        

for i in range(n+1):
    print(dp[i])