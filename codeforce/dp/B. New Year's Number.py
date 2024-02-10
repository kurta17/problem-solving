import sys
input = sys.stdin.readline

t= int(input())

for _ in range(t):
    n = int(input())
    m = n % 2020
    k = ((n-m)//2020) - m

    if k >= 0 and (k * 2020) + (m * 2021) == n:
        print("YES")
    else:
        print("NO")

