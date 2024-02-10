from functools import reduce


n = int(input())
nums = list(map(int, input().split()))
pre = [0 for i in range(n)]
ans = 0
for i in range(n):
    if nums[i] < -1:
        pre[i] = -1
        ans += -(nums[i]+1)
    elif nums[i] == -1:
        pre[i] = -1
    elif nums[i] == 1:
        pre[i] = 1
    elif nums[i] > 1:
        pre[i] = 1
        ans += (nums[i]-1)
    elif nums[i] == 0:
        pre[i] = 1
        ans += 1 

result = reduce(lambda x, y: x * y, pre)

if result == -1 and 0 not in nums:
    ans += 2
    print(ans)
else:
    print(ans)

