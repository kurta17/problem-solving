tt = int(input())

for _ in range(tt):
    n = int(input())
    mp = {}
    a = [input().split() for _ in range(3)]

    for i in range(3):
        for j in range(n):
            mp[a[i][j]] = mp.get(a[i][j], 0) + 1

    for i in range(3):
        tot = 0
        for j in range(n):
            if mp[a[i][j]] == 1:
                tot += 3
            elif mp[a[i][j]] == 2:
                tot += 1
        print(tot, end=' ')
    print()
