n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [1e9] * (x+1)
dp[0] = 0

for i in range(1, x+1):
    for j in c:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + 1)

if dp[x] == 1e9:
    print(-1)
else:
    print(dp[x])