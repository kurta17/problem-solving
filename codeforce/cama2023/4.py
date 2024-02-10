n = int(input())
count = 1
count2=-1
while count <= n:
    count *= 2
    count2 +=1
mylist = []
for i in range(count2):
    mylist.append(2**i)
if 2**count2 < n:
    mylist.append(n - 2**count2)
print(len(mylist))  
for x in sorted(mylist):
    print(x , end=" ")

# n = int(input())
# mylist = []
# a = 1
# while n >= a :
#     mylist.append(a)
#     a = a * 2
    
# b = n - (a//2)
# if b > 0:
#     mylist.append(b)
# mylist.sort()
# m = len(mylist)
# print(m + b)
# print(" ".join(map(str, mylist)))
