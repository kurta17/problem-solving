k,n,w = map(int,input().split())

amount = (w/2)*(2*k + (w -1)*k)
if amount > n:
    print(int(amount - n))
else:
    print(0)