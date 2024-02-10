n, a, b, c = map(int, input().split())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = float('-inf')

    if i - a >= 0:
        dp[i] = max(dp[i], dp[i - a] + 1)
    if i - b >= 0:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if i - c >= 0:
        dp[i] = max(dp[i], dp[i - c] + 1)

result = dp[n]
print(result)

