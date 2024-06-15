MOD = 10**9 + 7
string = "chokudai"

s = input().strip()
n = len(s)

dp = [0]*9
dp[0] = 1

for i in range(n):
    for j in range(8):
        if s[i] == string[j]:
            dp[j+1] += dp[j]
            dp[j+1] %= MOD

print(dp[8])