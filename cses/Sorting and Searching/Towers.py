import sys
input = sys.stdin.readline

n = int(input())
cubes = list(map(int, input().split()))

last_c = []

for c in cubes:
    placed = False
    for i in range(len(last_c)):
        if c < last_c[i]:
            last_c[i] = c
            placed = True
            break
    if not placed:
        last_c.append(c)

print(len(last_c))
