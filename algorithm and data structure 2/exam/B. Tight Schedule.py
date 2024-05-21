n,m = map(int,input().split())
minutes = list(map(int, input().split()))

minutes.sort()

ans = 0
i = 0

while i < n and m >= 0 and m - minutes[i] >= 0 and m >= minutes[0]:
    m -= minutes[i]
    ans += 1
    i += 1



print(ans)