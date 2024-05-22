import heapq

n,k = map(int, input().split())
time = list(map(int, input().split()))

if n <= k:
    print(max(time))
else:
    h = [0] * k
    for t in time:
        erl = heapq.heappop(h)
        new = erl + t
        heapq.heappush(h, new)

    print(max(h))
