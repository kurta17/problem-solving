import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
coeff = [0] * (max_a+1)
dp = [0] * (max_a+1)

for i in a:
    coeff[i] += 1

dp[0] = 0
dp[1] = coeff[1]

for i in range(2, max_a+1):
    dp[i] = max(dp[i-1], dp[i-2] + i*coeff[i])

print(dp[max_a])