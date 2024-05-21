n, s, f, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
inf = int(1e10)
dp = [[inf] * n for _ in range(k+1)]
dp[0][s] = 0

for i in range(1, k+1):
    for u in range(n):
        if dp[i-1][u] != inf: 
            for v in range(n):
                if a[u][v] != -1:
                    dp[i][v] = min(dp[i][v], dp[i-1][u] + a[u][v])

result = min(dp[i][f] for i in range(k+1))
if result >= inf:
    print(-1)
else:
    print(result)

