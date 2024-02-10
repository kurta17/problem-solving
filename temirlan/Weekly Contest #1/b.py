tl = list(map(str, input().split()))

num = []
char = []

for i in range(3):
    num.append(int(tl[i][0]))
    char.append(tl[i][1])

num.sort()
m = len(set(num))
n = len(set(char))

if n == 1 or m == 1 or (num[0] == num[1] and num[1] == num[2]):
    print(0)
elif n == 2 or (num[1] - num[0] <= 2) or (num[2] - num[1] <= 2) or (num[0] == num[1] or num[1] == num[2] or num[0] == num[2]):
    print(1)
else:
    print(2)







