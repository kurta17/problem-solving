n = int(input())
a = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = a[0]
dp[0][1] = 0



print(dp)