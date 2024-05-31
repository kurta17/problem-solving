n = int(input())    

grid = [[0 for i in range(101)] for j in range(101)]

for i in range(n):
    a,b,c,d = map(int, input().split())
    for i in range(a,b):
        for j in range(c,d):
            grid[i][j] = 1
            
    
result = 0
for i in range(101):
    result += sum(grid[i])

print(result)
