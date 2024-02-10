t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    station = list(map(int, input().split()))

    max_dist = station[0]
    for i in range(1, n):
        max_dist = max(max_dist, station[i] - station[i - 1])

    if max_dist > 2*(x - station[-1]):
        print(max_dist)
    elif max_dist < station[0]:
        print(station[0])
    else:
        print(2*(x - station[-1]))
