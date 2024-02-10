import sys
input = sys.stdin.readline

n,m = map(int,input().split())
l = []
for i in range(n+m):
    a= input()
    l.append(a)
mset = set(l)

if n > m:
    print("YES")   
elif n == m and  len(mset) & 1 == 1:
    print("YES")
else:
    print("NO")