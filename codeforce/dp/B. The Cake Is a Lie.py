import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())
    bar = (n-1) + (m-1)*n
    if k == bar:
        print("YES")
    else:
        print("NO")