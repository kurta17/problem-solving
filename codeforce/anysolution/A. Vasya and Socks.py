import sys
input = sys.stdin.readline

m, n = map(int, input().split())
ans = m + (m-1)//(n-1)

print(ans)