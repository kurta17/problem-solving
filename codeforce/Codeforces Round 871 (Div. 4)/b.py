t = int(input())

for _ in range(t):
    n = int(input())
    mylist = list(map(int, input().split()))
    res = 0
    result = 0
    for i in mylist:
        if i == 0:
            res += 1
        else:
            result = max(res, result)
            res = 0
    result = max(res,result)
    print(result)