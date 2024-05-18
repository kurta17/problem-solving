from heapq import heappush, heappop
from math import inf

n, m = map(int, input().split())
s, h = map(int, input().split())

G = [{} for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u][v] = w
    G[v][u] = w

dist = [inf] * n
prev = [None] * n
dist[s] = 0

heap = [(0, s)]
while heap:
    v = heappop(heap)[1]
    for u in G[v]:
        alt = dist[v] + G[v][u]
        if alt < dist[u]:
            dist[u] = alt
            prev[u] = v
            heappush(heap, (alt, u))

if dist[h] == inf:
    print(-1)
else:
    print(dist[h])
    path = []
    u = h
    while u is not None:
        path.append(u)
        u = prev[u]
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))