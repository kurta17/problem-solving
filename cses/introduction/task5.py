n = int(input())

newlist = []

if n == 1:
    print("1")
elif n <= 3:
    print("NO SOLUTION")
else:
    for i in range(2, n+1,2):
        newlist.append(str(i))
    for x in range(1,n+1,2):
        newlist.append(str(x))


print(" ".join(newlist))
