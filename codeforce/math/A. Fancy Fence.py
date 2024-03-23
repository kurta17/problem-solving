t = int(input())

for _ in range(t):
    a = int(input())
    gare = 180 - a
    k = 360 // gare
    if k * gare == 360:
        print("YES")
    else:
        print("NO")