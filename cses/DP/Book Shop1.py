n,x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0]*(x+1)
for i in range(n):
    for j in range(x, prices[i]-1, -1):
        dp[j] = max(dp[j], dp[j-prices[i]] + pages[i])

print(dp[x])