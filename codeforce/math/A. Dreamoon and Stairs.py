n, m = map(int, input().split())

stepm = (n+1) // 2

mod = stepm % m
if n>=m and mod == 0:
    print(stepm)
elif n>=m and mod != 0:
    print(stepm + (m-mod))
else:
    print(-1)