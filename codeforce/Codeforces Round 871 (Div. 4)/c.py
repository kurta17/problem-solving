t = int(input())
for _ in range(t):
    n = int(input())
    mydict = {"00": 10**9, "01": 10**9, "10": 10**9, "11": 10**9}
    answer = 10**9
    for _ in range(n):
        x, s = input().split()
        x = int(x)
        mydict[s] = min(mydict[s], x)

    if min(mydict["11"], mydict["10"] + mydict["01"]) > 10**6:
        print("-1")
    else:
        print(min(mydict["11"], mydict["10"] + mydict["01"]))

    
