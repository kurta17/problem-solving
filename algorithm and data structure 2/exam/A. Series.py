n,a = map(int, input().split())


ans = 0

if a == 1:
    s = (1 + n) * ( n // 2)
    print(s)
else:
    for i in range(1,n+1):
        ans += (i * (a ** (i)))
    print(ans)

