def low_function(graph, u, visited, parent, low, disc, bridge):
    visited[u] = True
    low[u] = disc[u] = low_function.time
    low_function.time += 1
    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            low_function(graph, v, visited, parent, low, disc, bridge)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridge.append((u, v))
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

# Define the graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1, 4],
    4: [3]
}

# Initialize the necessary variables
n = len(graph)
visited = [False] * n
parent = [-1] * n
low = [float('inf')] * n
disc = [float('inf')] * n
bridge = []
low_function.time = 0

# Call the function
low_function(graph, 0, visited, parent, low, disc, bridge)

# Print the bridges
print(bridge)  # Output: [(3, 4), (1, 3)]