def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  # Initialize the result to -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            result = mid  # Update the result when the condition is satisfied
            left = mid + 1
        else:
            right = mid - 1
    return result

n, m = map(int, input().split())
t = list(map(int, input().split()))
c = list(map(int, input().split()))
t.sort()

for max_price in c:
    ind = binary_search(t, max_price)
    if ind == -1:  
        print(-1)
    else:
        print(t[ind])  
        t.pop(ind)  

