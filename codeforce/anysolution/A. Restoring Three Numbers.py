import sys
input = sys.stdin.readline

x = list(map(int, input().split()))

s = sum(x)//3

for i in x:
    if s - i > 0:
        print(s - i, end=" ")

