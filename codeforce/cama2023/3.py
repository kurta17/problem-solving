n, k = map(int, input().split())
mylist= sorted(list(map(int, input().split())))
mylist = mylist[-(k):]
res = sum(mylist)
print(res)



