import math
h = int(input())

dp = [0] * (h //2 + 1)
dp[0] = h
for i in range(h//2 + 1):
    if dp[i] == 1:
        break
    dp[i+1] = dp[i] // 2

print(sum(dp))

# ans = 0
# curr = 1

# while h > 1:
#     ans += curr
#     curr *= 2
#     h //= 2

# ans += curr    
# print(ans)