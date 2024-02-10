t = int(input())

for o in range(t):
    n, k = map(int, input().split())
    s = input()

    left = 0
    move = 1
    result = 0

    while move <= n:
        consecutive_white = 0

        for x in range(k):
            if move <= n and s[move - 1] == 'B':  
                consecutive_white += 1
            move += 1

        result += 1 

        if consecutive_white > 0:
            left = move - 1  
        else:
            left = move   

    print(result - 1) 

