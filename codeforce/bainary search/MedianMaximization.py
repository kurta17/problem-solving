t = int(input())

for _ in range(t):
    n, s = map(int, input().split())

    if n == 1:
        print(s)
    elif s == 1:
        print(0)
    else:
        med_pos = (n + 1) // 2
        max_median = s // (n - med_pos + 1)
        print(max_median)
