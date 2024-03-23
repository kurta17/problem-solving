import sys
input = sys.stdin.readline
def can_make_zero(n, arr):
    i = 0
    while i < n-2:
        if arr[i] >= 0:
            k = arr[i] 
            arr[i] -= k 
            arr[i+1] -= k * 2
            arr[i+2] -= k 
            i += 1
        else:
            break

    return all(x == 0 for x in arr)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if can_make_zero(n, arr):
        print("YES")
    else:
        print("NO")
