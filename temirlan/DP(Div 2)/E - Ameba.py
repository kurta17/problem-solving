n = int(input())
a = list(map(int, input().split()))

m = 2 *n + 1
dp = [-1] * (m + 1)
dp[1] = 0

for i in range(1,n+1):
    p = a[i-1]
    child1 = 2 * i
    child2 = 2 * i + 1
    dp[child1] = dp[p] + 1
    dp[child2] = dp[p] + 1

for i in range(1,m+1):
    print(dp[i])