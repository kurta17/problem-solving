import math
n, m = map(int, input().split())
a = list(map(int, input().split()))
lights = []
cord = []
for i in range(n):
    x,y = list(map(int, input().split()))
    if i+1 in a:
        lights.append((x,y))
    else:
        cord.append((x,y))

distance = 0

for i in range(len(cord)):
    temp = float('inf')
    for x,y in lights:
        d_max = math.sqrt((abs(x - cord[i][0])) ** 2 + (abs(y - cord[i][1]))**2)
        temp = min(temp, d_max)
    distance = max(distance, temp)

print(distance)

        
