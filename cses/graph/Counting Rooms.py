n,m = map(int, input().split())
graph = [list((input())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
ans = 0

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or visited[x][y] or graph[x][y] == '#':
        return
    visited[x][y] = True
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '.' and not visited[i][j]:
            # check every "." connected to this cell
            dfs(i, j)
            ans += 1

print(ans)


            