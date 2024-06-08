from collections import defaultdict

n = int(input())

dx = defaultdict(int)
dy = defaultdict(int)
dxy = defaultdict(int)
ans = 0

for _ in range(n):
    x, y = map(int, input().split())
    ans += dx[x] + dy[y] - dxy[(x,y)]
    dx[x] += 1
    dy[y] += 1
    dxy[(x,y)] += 1
    

print(ans)