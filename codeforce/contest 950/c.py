from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    orig = list(map(int, input().split()))
    mod = list(map(int, input().split()))
    m = int(input())
    val = list(map(int, input().split()))

    modification_count = defaultdict(int)
    for value in val:
        modification_count[value] += 1

    possible = True
    for i in range(n):
        if orig[i] != mod[i]:
            if modification_count[mod[i]] > 0:
                modification_count[mod[i]] -= 1
            else:
                possible = False
                break

    if val[-1] not in mod:
        possible = False

    if possible:
        print("YES")
    else:
        print("NO")
