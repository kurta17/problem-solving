from collections import defaultdict

def dfs(G, starting_point):
    visited = [False] * (n+1)
    stack = [starting_point]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(G[node])

    return visited

n,m,sp = map(int,input().split())

G = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = dfs(G, sp)

ans = 0

for i in visited:
    if i:
        ans += 1

print(ans)



