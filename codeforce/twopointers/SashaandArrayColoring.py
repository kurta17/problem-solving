t = int(input())

for _ in range(t):
    n = int(input())
    mlist = sorted(map(int, input().split()))
    
    left = 0
    right = n - 1
    result = 0
    while left < right:
        result += mlist[right] - mlist[left]
        right -= 1
        left += 1
    print(result)




