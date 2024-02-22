n = int(input())

def middle_element(n):
    return ((n+1)//2) ** 2

def kth_element(n, k):
    left, right = 1, n*n
    while left < right:
        mid = (left + right) // 2
        if count(mid,n) < k:
            left = mid + 1
        else:
            right = mid
    return left

def count(mid, n):
    total = 0
    for i in range(1, n+1):
        minimum = min(mid // i, n)
        total += minimum
    return total

print(count(3,4))
