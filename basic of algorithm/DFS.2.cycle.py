#make a dfs which check if we meet a cycle or not and calculate the number of cycles

def count_cycle(g,n):
    def dfs(v,par):
        visited[v] = True
        for i in g[v]:
            if not visited[i]:
                if dfs(i,v):
                    return True
            elif i != par:
                return True
        return False
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            if dfs(i,-1):
                count += 1
    return count
        
#test
n = 5
g = [
    [1,3],
    [0, 2],
    [1,2],
    [4],
    [3]
]
print(count_cycle(g,n)) 