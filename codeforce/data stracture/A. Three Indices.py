import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    found = False
    for i in range(1, n - 1):
        if p[i - 1] < p[i] and p[i] > p[i + 1]:
            print("YES")
            print(i, i + 1, i + 2)
            found = True
            break

    if not found:
        print("NO")







