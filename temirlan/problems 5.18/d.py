n = 200
coins = [7, 5, 11]

dp = [0] * (n + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, n + 1):
        dp[i] += dp[i - coin]

print(dp[n])