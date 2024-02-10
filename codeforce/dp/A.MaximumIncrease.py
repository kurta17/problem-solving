import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

count = 1 
max_count = 1 

ind = 0

while ind < n - 1:
    if nums[ind] < nums[ind + 1]:
        count += 1
        ind += 1
    else:
        max_count = max(max_count, count)
        count = 1
        ind += 1

max_count = max(max_count, count)

print(max_count)




