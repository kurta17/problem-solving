import sys
input = sys.stdin.readline

n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (x+1)
dp[0] = 1

for coin in c:
    for i in range(coin, x+1):
        dp[i] = (dp[i] + dp[i-coin]) % (10**9 + 7)

print(dp[x])