h,w = map(int,input().split())

l = [['.']* (w+1)]
dp = [[0]*(w+1) for i in range(h+1)]
dp[0][1] = 1
count = 0
for i in range(h):
    a = list(input())
    a = ['.'] + a
    l.append(a)

for i in range(1,h+1):
    for k in range(1,w+1):
        if l[i][k] == '.':
            if dp[i][k-1] != 0:
                dp[i][k] = dp[i][k-1] + 1
            elif dp[i-1][k] != 0:
                dp[i][k] = dp[i-1][k] + 1
        else:
            dp[i][k] = 0
ans = 0
for i in dp:
    ans = max(ans,max(i))
print(ans-1)
