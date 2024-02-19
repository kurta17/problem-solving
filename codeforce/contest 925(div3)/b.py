t= int(input())
for _ in range(t):
    n = int(input())
    wat = list(map(int, input().split()))
    equ = sum(wat) // n
    ved = 0
    i = 0
    ans = True
    while i < n :
        if wat[i] > equ:
            ved += wat[i] - equ
            i+=1
        else:
            k = equ - wat[i]
            ved -= k
            if ved < 0:
                ans = False
                break
            i+= 1
    if ans:
        print("YES")
    else:
        print("NO")

