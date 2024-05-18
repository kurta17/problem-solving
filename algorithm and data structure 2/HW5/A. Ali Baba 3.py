W, N = map(int, input().split())

weight = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (W + 1) for _ in range(N + 1)]
keep = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, W + 1):
        if weight[i-1] <= w and c[i-1] + dp[i-1][w - weight[i-1]] > dp[i-1][w]:
            dp[i][w] = c[i-1] + dp[i-1][w - weight[i-1]]
            keep[i][w] = 1
        else:
            dp[i][w] = dp[i-1][w]

items = []
w = W
for i in range(N, 0, -1):
    if keep[i][w] == 1:
        items.append(i)
        w -= weight[i-1]

items.reverse()

print(dp[N][W])
print(len(items))
print(' '.join(map(str, items)))