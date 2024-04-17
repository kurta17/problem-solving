t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    if k >= n:
        print(k // n)
    else:
        result = (k + n - 1) // n
        print(result)


