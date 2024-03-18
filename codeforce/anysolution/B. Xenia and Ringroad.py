import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = list(map(int, input().split()))
i = 1
ans = a[0] - 1

while i < m:
    if a[i-1] > a[i]:
        ans += (n - a[i-1] + a[i])
        i+=1
    else:
        ans += (a[i] - a[i-1] )
        i+=1

print(ans)


