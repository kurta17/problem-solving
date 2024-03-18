from typing import List
from collections import deque

def size_of_largest_component_using_bfs(graph: List[List[int]]) -> int:
    n = len(graph)
    visited = [False] * n
    max_size = 0

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            size = 0
            while queue:
                node = queue.popleft()
                size += 1
                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True

            max_size = max(max_size, size)
    return max_size

def size_of_largest_component_using_dfs(graph: List[List[int]]) -> int:
    n = len(graph)
    visited = [False] * n
    max_size = 0

    def dfs(node):
        visited[node] = True
        size = 1

        for neighbour in graph[node]:
            if not visited[neighbour]:
                size += dfs(neighbour)

        return size

    for i in range(n):
        if not visited[i]:
            size = dfs(i)
            max_size = max(max_size, size)

    return max_size

graph = [[1, 2], [0, 2], [0, 1, 3], [2, 4], [3], [7], [], [5]]
assert size_of_largest_component_using_bfs(graph) == 5
assert size_of_largest_component_using_dfs(graph) == 5
print(size_of_largest_component_using_bfs(graph),size_of_largest_component_using_dfs(graph))