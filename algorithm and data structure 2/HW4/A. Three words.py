from math import inf
from bisect import bisect_left

n = int(input())
sequence = list(map(int, input().split()))

dp = [inf] * (n + 1)
dp[0] = -inf

for i in range(n):
    j = bisect_left(dp, sequence[i])
    dp[j] = sequence[i]

print(max(i for i in range(n+1) if dp[i] < float('inf')))