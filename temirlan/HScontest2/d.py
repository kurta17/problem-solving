t = int(input())

for i in range(t):
    mlist = []
    n, x = map(int, input().split())
    for o in range(n):
        d , h = list(map(int, input().split()))
        diff = d - h
        mlist.append(diff)
    maxcut = max(mlist)
    count = 0
    if maxcut < 0:
        print("-1")
    else:
        while x > - maxcut + 1:
            count += 1
            x -= maxcut
        print(count-1)
        
        

    
    
