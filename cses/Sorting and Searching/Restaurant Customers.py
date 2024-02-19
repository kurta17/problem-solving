import sys
input = sys.stdin.readline

n = int(input())
times = []

for i in range(n):
    start, end = map(int, input().split())
    times.append((start, 1))
    times.append((end, -1))

times.sort()
ans = 0
current = 0

for t,p in times:
    current += p
    ans = max(ans, current)

print(ans)