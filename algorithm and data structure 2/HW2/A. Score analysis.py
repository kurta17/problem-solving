def bsearch_l(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r

def bsearch_r(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] > key:
            r = m
        else:
            l = m
    return r

N, M = map(int, input().split())
scores = sorted(map(int, input().split()))

for _ in range(M):
    l, r = map(int, input().split())
    print(bsearch_r(scores, r) - bsearch_l(scores, l))