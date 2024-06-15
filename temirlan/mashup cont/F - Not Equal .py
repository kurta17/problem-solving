n = int(input())
c = list(map(int, input().split()))

c.sort()
ans = 1

for i in range(n):
    if c[i] < i:
        ans = 0
        break
    else:
        ans = (ans * (c[i] - i )) % (10**9 + 7)

print(ans)

