n = int(input())
cordinates = list(map(int, input().split()))
cordinates.sort()


dp = [[0] * n for _ in range(2)]
dp[0][0] = float('inf')
dp[1][0] = 0


for i in range(1, n):
    dp[0][i] = min(dp[0][i - 1], dp[1][i - 1]) + (cordinates[i] - cordinates[i - 1])
    dp[1][i] = dp[0][i - 1]


print(dp[0][-1])

