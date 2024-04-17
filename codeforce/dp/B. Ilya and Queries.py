import sys
input = sys.stdin.readline

s = str(input())
dp = [0] * len(s)
for i in range(1, len(s)):
    dp[i] = dp[i-1]
    if s[i] == s[i-1]:
        dp[i] += 1

n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    print(dp[r-1] - dp[l-1])