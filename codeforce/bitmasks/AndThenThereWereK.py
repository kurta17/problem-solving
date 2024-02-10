t = int(input())
for _ in range(t):
    n = int(input())
    l = 0
    for i in range(30):
        if ((n >> i) & 1) == 1:
            l = i
    print((1 << l) - 1)
