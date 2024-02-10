n = int(input())
mlist= []
for i in range(n):
    a = list(map(int,input().split()))
    mlist.append(a)
sumx = 0
sumy = 0
sumz = 0  
for i in mlist:
    sumx =sumx + i[0]
    sumy =sumy + i[1]
    sumz =sumz + i[2]  
    
if sumx== 0 and sumy== 0 and sumz == 0:
    print("YES")
else:
    print("NO")

