n = int(input())
number = list(map(int, input().split()))
num = []
for i in number:
    if i not in num:
        num.append(i)
num.sort()

if len(num) == 3 and (num[1] - num[0] == num[2] - num[1]):
    print(num[1] - num[0])
elif len(num) == 2 and ((num[1] - num[0]) % 2 == 0):
    print((num[1] - num[0]) // 2)
elif len(num) == 2 and ((num[1] - num[0]) % 2 != 0): 
    print(num[1] - num[0])
elif len(num) == 1:
    print(0)
else:
    print(-1)



