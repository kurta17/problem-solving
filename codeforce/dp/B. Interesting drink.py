n = int(input())
x = list(map(int, input().split()))
x.sort()

q = int(input())

for _ in range(q):
    ans = 0  # Move initialization outside the loop
    l = 0
    r = n - 1
    coin = int(input())
    while l <= r:
        mid = l + (r - l) // 2

        if x[mid] <= coin:
            l = mid + 1
        else:
            r = mid - 1
    res = l
    print(res)







