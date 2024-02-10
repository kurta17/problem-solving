t = int(input())

for _ in range(t):
    n = int(input())
    numlist = list(map(int, input().split()))
    numlist.sort()

    if n == 1:
        print(0)
    else:
        mydict = {}
        for i in range(n):
            if numlist[i] not in mydict:
                mydict[numlist[i]] = 1
            else:
                mydict[numlist[i]] += 1
        
        result = 0
        for key in mydict:
            if mydict[key] > 1:
                result += (mydict[key] * (mydict[key] - 1)) // 2  
        print(result)

