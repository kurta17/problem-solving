t = int(input())

for _ in range(t):
    n = int(input())
    numlist = list(map(int, input().split()))
    
    result = numlist[0]
    current_sum = numlist[0]

    for i in range(1, n):
        if (numlist[i - 1] % 2 != 0 and numlist[i] % 2 == 0) or (numlist[i - 1] % 2 == 0 and numlist[i] % 2 != 0):
            current_sum = max(numlist[i], current_sum + numlist[i])
            result = max(result, current_sum)
        else:
            current_sum = numlist[i]
            result = max(result, current_sum)

    print(result)


