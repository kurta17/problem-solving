import sys
input = sys.stdin.readline

n,m = map(int, input().split())
broken = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1 if 1 not in broken else 0

for i in range(2, n + 1):
    if i in broken:
        continue
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

print(dp[n])

