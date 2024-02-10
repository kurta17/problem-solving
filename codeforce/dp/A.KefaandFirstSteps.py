import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
count = 1
max_count = 1
i = 1

while i < n:
    if nums[i-1] <= nums[i]:
        count += 1
        i += 1
    else:
        max_count = max(max_count, count)
        count = 1
        i +=1
ans = max(max_count,count)
print(ans)
    