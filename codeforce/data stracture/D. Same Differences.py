t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    table = {}
    res = 0
    for i in range(n):
        diff = a[i] - i
        if diff in table:
            res += table[diff]
        table[diff] = table.get(diff, 0) + 1

    print(res)

             