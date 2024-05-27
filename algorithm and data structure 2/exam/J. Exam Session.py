import sys
input = sys.stdin.readline

def func(N, K, M, usage):
    from collections import deque

    next_use = [deque() for _ in range(N + 1)]
    for i in range(M - 1, -1, -1):
        next_use[usage[i]].appendleft(i)

    table = set()
    count = 0

    for k, book in enumerate(usage):
        next_use[book].popleft()
        
        if book in table:
            continue

        if len(table) < K:
            table.add(book)
        else:
            farthest = -1
            evict = None
            for b in table:
                if not next_use[b]:
                    evict = b
                    break
                elif next_use[b][0] > farthest:
                    farthest = next_use[b][0]
                    evict = b

            table.remove(evict)
            table.add(book)
        
        count += 1
    return count


N, K, M = map(int, input().split())
usage = list(map(int, input().split()))
count = func(N, K, M, usage)
print(count)