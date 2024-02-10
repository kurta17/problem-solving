n = int(input())
nums = list(map(int, input().split()))

nums_suf = [0] * (n+1)
for i in range(1, n + 1):
    nums_suf[i] = nums_suf[i - 1] +  nums[i-1]

print(" ".join(map(str, nums_suf)))
