n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
i = 0
j = n - 1
ans = 0
have_gondola_yet = [False] * n

while i < j:
    if p[i] + p[j] > x:
        j -= 1
    else:
        ans += 1
        have_gondola_yet[i] = have_gondola_yet[j] = True
        i += 1
        j -= 1

for i in range(n):
    if not have_gondola_yet[i]:
        ans += 1

print(ans)










# n,x = map(int, input().split())
# w = list(map(int,input().split()))
# w.sort()

# count = 0
# i = 0
# j = n - 1

# while i < n - 1 and j > i:
#     if w[i] + w[j] <= x:
#         count += 1
#         w[j] = 100 ** 10
#         i += 1
#         j = n - 1
#     else:
#         j -= 1

# print(count)


    