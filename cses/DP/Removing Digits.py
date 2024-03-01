n = int(input())

dp = [0] + [float('inf')] * n
for i in range(1, n + 1):
    for digit in map(int, str(i)):
        if i - digit >= 0:
            dp[i] = min(dp[i], 1 + dp[i - digit])

def rec(n):
    if n == 0:
        return 0
    ans = float('inf')
    for digit in map(int, str(n)):
        if n - digit >= 0:
            ans = min(ans, 1 + rec(n - digit))
    return ans

print(dp[n])
print(rec(n))

