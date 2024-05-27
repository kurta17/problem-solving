from collections import deque

def path_poss(up_to, n, m, trees):
    grid = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(up_to):
        x, y = trees[i][0], trees[i][1]
        grid[x][y] = -1

    dic = [(1, 0), (0, 1)]

    if grid[0][0] == -1 or grid[n - 1][m - 1] == -1:
        return False

    queue = deque()
    queue.appendleft((0, 0))

    while queue:
        x, y = queue.pop()
        grid[x][y] = 1

        for dx, dy in dic:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0:
                    queue.append((nx, ny))

    return grid[n - 1][m - 1] == 1

n, m, k = map(int, input().split())
trees = [tuple(map(int, input().split())) for _ in range(k)]

left, right = 1, k
ans = 0
path_exists = False

while left <= right:
    mid = (left + right) // 2

    if path_poss(mid, n, m, trees):
        ans = max(ans, mid)
        path_exists = True
        left = mid + 1
    else:
        right = mid - 1

if ans == k and path_exists:
    print(-1)
else:
    print(ans)
