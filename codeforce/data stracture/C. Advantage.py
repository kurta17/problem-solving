import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)

    for i in range(n):
        if a[i] == b[n - 1]:
            print(a[i] - b[n - 2], end=" ")
        else:
            print(a[i] - b[n - 1], end=" ")
    
    print()


