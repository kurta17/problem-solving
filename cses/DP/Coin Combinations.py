import sys
input = sys.stdin.readline

n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (x+1)
dp[0] = 1

for i in range(1, x+1):
    for j in c:
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i-j]) % (10**9 + 7)
            

print(dp[x])