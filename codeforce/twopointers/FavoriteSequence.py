t = int(input())

for i in range(t):
    n = int(input())
    ml = list(map(int, input().split()))

    a = [0] * n
    

    right = n -1
    left = 0

    a[0] = ml[0]

    for i in range(n):
        if i % 2 == 0:
            a[i] = ml[left] 
            left += 1
        else:
            a[i] = ml[right]
            right -= 1
    print(" ".join(map(str, a)))

    


