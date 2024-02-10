t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    if n == 1:
        print(c[0] - 1)
    else:
        result = c[0] - 1 
        for i in range(1, n):
            if c[i] > c[i - 1]:
                result += c[i] - c[i - 1]

        print(result)
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = max(0, a[-1] - 1)

    for i in range(n - 2, -1, -1):
        ans += max(0, a[i] - a[i + 1])

    print(ans)





