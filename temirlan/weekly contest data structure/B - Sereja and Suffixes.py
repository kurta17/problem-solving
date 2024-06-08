n,q = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * n
distinct = set()

for i in range(n-1, -1, -1):
    distinct.add(a[i])
    dp[i] = len(distinct)


for i in range(q):
    l = int(input())
    print(dp[l-1])




