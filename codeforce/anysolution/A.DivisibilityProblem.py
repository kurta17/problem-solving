t = int(input())

for _ in range(t):
    a , b = map(int, input().split())
    k = ((a // b) + 1) * b
    if a % b == 0:
        print(0)
    else:
        print(k - a)
