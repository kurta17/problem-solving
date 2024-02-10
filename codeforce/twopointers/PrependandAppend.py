t = int(input())

for _ in range(t):
    n = int(input())
    l = input()
    left  = 0
    right = n - 1

    while left <= right:
        if l[left] != l[right]:
            left += 1
            right -= 1
        else:
            break


    print(right - left + 1)
