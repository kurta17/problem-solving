n, l = map(int, input().split())
lamps = list(map(int, input().split()))

lamps.sort()

max_distance = max(lamps[0], l - lamps[-1])

for i in range(1, n):
    max_distance = max(max_distance, (lamps[i] - lamps[i-1]) / 2)

print(max_distance)
