n,m = map(int, input().split())
node = int(input())
value_country = list(map(int, input().split()))

pairs = []
for _ in range(m):
    a,b = map(int, input().split())
    pairs.append((a,b))

def bfs(node):
    total_sum = 0
    visited = [False] * (n+1)
    queue = []
    queue.append(node)
    visited[node] = True
    while queue:
        s = queue.pop(0)
        for (a,b) in pairs:
            if a == s and not visited[b]:
                queue.append(b)
                visited[b] = True
                total_sum += value_country[b-1]
            elif b == s and not visited[a]:
                queue.append(a)
                visited[a] = True
                total_sum += value_country[a-1]
    return total_sum




