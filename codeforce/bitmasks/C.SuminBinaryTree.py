import sys
input = sys.stdin.readline


t= int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    while n > 0:
        ans += n
        n = n >> 1
    print(ans)


