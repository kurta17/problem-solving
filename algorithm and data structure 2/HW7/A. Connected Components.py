### recursive DFS
# def dfs(G,visited,i):
#     visited[i] = True
#     for j in G[i]:
#         if not visited[j]:
#             dfs(G,visited,j)

### iterative DFS

def dfs(G,visited,i):
    comp = []
    stack = [i]
    while stack:            
        i = stack.pop()
        comp.append(i)
        visited[i] = True
        for j in G[i]:
            if not visited[j]:
                stack.append(j)
    return comp

n,m = map(int,input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False]*n
compontents = []
count = 0

for i in range(n):
    if not visited[i]:
        compontents.append(set(dfs(G,visited,i)))
        count += 1


print(count)
for comp in compontents:
    print(len(comp))
    print(*comp)

