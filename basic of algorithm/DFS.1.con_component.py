def con_component(n, edges):
    def dfs(v):
        visited[v] = True
        for i in edges[v]:
            if not visited[i]:
                dfs(i)
                
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count
n = 5
edges = [
    [1],
    [0, 2],
    [1],
    [4],
    [3]
]
print(con_component(n, edges))  