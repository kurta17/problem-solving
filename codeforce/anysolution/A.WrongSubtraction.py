n, k = map(int, input().split())

    
if n < 10:
    print(n - k)
else:
    while k > 0:
        if n % 10 == 0:
            n = n // 10
        else:
            n -= 1
        k -= 1
    print(n)



