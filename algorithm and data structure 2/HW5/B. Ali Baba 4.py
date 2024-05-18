n = int(input())
cost = list(map(int, input().split()))

total = sum(cost)

half = total // 2

if total % 2 != 0:
    print("NO")
    
else:
    dp = [False] * (half + 1)
    dp[0] = True

    for i in range(n):
        for j in range(half, cost[i] - 1, -1):
            if dp[j - cost[i]]:
                dp[j] = True

    if dp[half]:
        print("YES")
    else:
        print("NO")