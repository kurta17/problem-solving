n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if b == 0:
        print(1)
    elif a == 0:
        print(0)
    elif a ** b > 10**9 + 7:
        print(a ** b % 10**9 + 7)
    else:
        print(a ** b)