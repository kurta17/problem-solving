n, x = map(int, input().split())
jumps = []  

for _ in range(n):
    a, b = map(int, input().split())
    jumps.append((a, b))

dp = [[False] * (x + 1) for _ in range(n + 1)]
dp[0][0] = True  

for i in range(1, n + 1):
    a, b = jumps[i - 1]
    for j in range(x + 1):
        if dp[i - 1][j]:
            if j + a <= x:
                dp[i][j + a] = True
            if j + b <= x:
                dp[i][j + b] = True

if dp[n][x]:
    print("Yes")
else:
    print("No")