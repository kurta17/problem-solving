k, r = map(int, input().split())
ans = 1
last = k % 10
while (k * ans) % 10 != 0 and (last * ans) % 10 != r:
    ans += 1

print(ans)
