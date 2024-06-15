t= int(input())

for _ in range(t):
    n = int(input())
    msum = 0
    x = 2
    for i in range(2,n+1):
        k = n//i
        sum = i*(k*(k+1))//2
        if sum > msum:
            msum = sum
            x = i
    print(x)
        
