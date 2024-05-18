from collections import deque

def bfs(matrix, start, end):
    n, m = len(matrix), len(matrix[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(start, 0)])
    
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and matrix[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append(((nx, ny), steps + 1))
    return -1

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
start = end = None

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'E':
            start = (i, j)
        elif matrix[i][j] == 'X':
            end = (i, j)
print(bfs(matrix, start, end))


