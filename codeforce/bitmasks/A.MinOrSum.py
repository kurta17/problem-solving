import sys
input = sys.stdin.readline


t= int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(len(a)):
        x = x | a[i]
    print(x)
