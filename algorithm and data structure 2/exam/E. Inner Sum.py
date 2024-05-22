n = int(input())
nums = list(map(int, input().split()))

poss = set()

for i in range(n):
    for j in range(i + 1, n):
        poss.add(nums[i] + nums[j])

ans = 0
for i in nums:
    if i in poss:
        ans += 1

print(ans)
    