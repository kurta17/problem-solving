n = int(input())
count = 0
for i in range(n):
    mlist = list(map(int, input().split()))
    if sum(mlist) > 1:
        count += 1
    else:
        continue
print(count)
