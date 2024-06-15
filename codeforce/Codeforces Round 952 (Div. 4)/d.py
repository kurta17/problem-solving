n = int(input())  # Number of test cases

for _ in range(n):
    n, m = map(int, input().split())  # Dimensions of the grid
    grid = []
    for i in range(n):
        grid.append(list(input()))
    
    cord = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                cord.append((i, j))
    
    if len(cord) == 1:
        ans = (cord[0][0] + 1, cord[0][1] + 1)  
        print(ans[0], ans[1])
    else:
        w_min = float('inf')
        w_max = float('-inf')
        h_min = float('inf')
        h_max = float('-inf')
        
        for i in cord:
            w_max = max(w_max, i[1])
            w_min = min(w_min, i[1])
            h_max = max(h_max, i[0])
            h_min = min(h_min, i[0])
        
        ans = ((h_max + h_min) // 2 + 1, (w_max + w_min) // 2 + 1)
        print(ans[0], ans[1])
