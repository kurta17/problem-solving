t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == 0 or b == 0:
        print(0)
    elif (a+b)>=4 and (a == 1 or b == 1):
        print(1)
    elif a >= 2 and b >= 2:
        maxteam = (a + b) / 4
        teams = min(maxteam, min(a, b) )
        print(int(teams))
    else:
        print(0)
    
    


