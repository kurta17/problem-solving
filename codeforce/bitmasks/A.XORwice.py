import sys
input = sys.stdin.readline


t= int(input())
for _ in range(t):
    a,b = map(int, input().split())

    c = a & b

    print((a ^ c) +( b ^ c))