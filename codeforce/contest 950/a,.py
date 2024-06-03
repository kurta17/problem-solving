t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    a = str(input())
    ans = 0
    ca = 0
    cb = 0
    cc = 0
    cd = 0
    ce = 0
    cf = 0
    cg = 0

    for i in a:
        if i == 'A' and ca < m:
            ca += 1
        elif i == 'B' and cb < m:
            cb += 1
        elif i == 'C' and cc < m:
            cc += 1
        elif i == 'D' and cd < m:
            cd += 1
        elif i == 'E' and ce < m:
            ce += 1
        elif i == 'F' and cf < m:
            cf += 1
        elif i == 'G' and cg < m:
            cg += 1

    ans = (m - ca) + (m - cb) + (m - cc) + (m - cd) + (m - ce) + (m - cf) + (m - cg)
    print(ans)