import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

w = [0] * (n+1)

for i in range(1,n+1):
    w[i] = w[i-1] + a[i-1]


for k in b:
    
    l = 0
    r = n

    while l < r:
        m = (l + r) // 2
        if w[m] < k:
            l = m + 1
        else:
            r = m
    print(l)


