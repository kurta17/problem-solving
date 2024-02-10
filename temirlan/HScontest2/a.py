n, k = map(int, input().split())
colorlist = list(map(int, input().split()))

a = 1  
b = 1 

for i in range(1, len(colorlist)):
    if colorlist[i] != colorlist[i - 1]:
        a += 1
    else:
        b = max(b, a)
        a = 1  


b = max(b, a)

print(b)


    
