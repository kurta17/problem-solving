n = int(input())
h = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = 0


for i in range(n-1):
    if h[i] >= h[i+1]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 0

print(max(dp))
