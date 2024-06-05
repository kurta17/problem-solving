n = int(input())
a = list(map(int, input().split()))

called = [False] * n
i = 0
while i < n:
    if not called[i]:
        called[a[i] - 1] = True
    i += 1

count = 0
ans = []
for i in range(n):
    if not called[i]:
        count += 1
        ans.append(i+1)

print(count)
print(*ans)
