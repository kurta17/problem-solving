n = int(input())
nlist = []
for i in range(n):
    m = list(map(int, input().split()))
    nlist.append(m)

def find(n, k):
    while n > 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k // 2 + 1
        n //= 2
    return k
for x in nlist:
    res = find(x[0],x[1])
    print(res)

