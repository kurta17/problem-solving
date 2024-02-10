s, n = map(int, input().split())

stren = []
for i in range(n):
    x, y = map(int, input().split())
    if s > x:
        s += y
    else:
        stren.append((x, y))

stren.sort(key=lambda x: x[0])

for i in range(len(stren)):
    if s > stren[i][0]:
        s += stren[i][1]
    else:
        break

if len(stren) == 0 or s > stren[-1][0]:
    print("YES")
else:
    print("NO")

