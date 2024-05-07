
x = 10**6
d = [0 for i in range(1,x+1)]

for i in range(1,x+1):
    for k in range(i,x,i):
        d[i] += 1

for i in range(1,x+1):
    if d[i] == 320:
        print(i)
        exit(0)