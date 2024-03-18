import sys
input = sys.stdin.re
def can_make_zero(n, arr):
    for i in range(1, n-1):
        if arr[i] >=2 and arr[i] >= arr[i-1] and arr[i-1]>=1 and arr[i+1]>=1 and arr[i] >= arr[i+1]:
            arr[i] -= 2
            arr[i-1] -= 1
            arr[i+1] -= 1
            can_make_zero(n, arr)
        elif i < n-2:
            i+=1

    return all(x == 0 for x in arr)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if can_make_zero(n, arr):
        print("YES")
    else:
        print("NO")
