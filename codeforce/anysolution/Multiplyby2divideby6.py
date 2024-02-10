t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(0)
    else:
        result = 0
        while n > 1:
            if n % 6 == 0:
                n = n // 6
                result += 1
            elif n % 3 == 0:
                n = n * 2
                result += 1
            else:
                print(-1)
                break
        else:
            print(result)


    