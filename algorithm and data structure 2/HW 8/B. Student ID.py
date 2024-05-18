n, s, f, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
inf = int(1e9)
dp = [[inf] * (n+4) for _ in range(n+4)]
dp[0][s] = 0

for i in range(1, k+1):
    for u in range(n):
        
        for v in range(n):
            if a[u][v] != -1 and dp[i-1][u] != inf:
                dp[i][v] = min(dp[i][v], dp[i-1][u] + a[u][v])

if dp[k][f] >= inf:
    print(-1)
else:
    print(dp[k][f])
