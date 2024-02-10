# n = int(input())
# new_list = []
# for i in range(n):
#     xylist = list(map(int, input().split()))
#     new_list.append(xylist)
    
# print(new_list)

num = int(input())
pairs = []
for x in range(num):
    pair = (input())
    nums = pair.split()
    pairs.append((int(nums[0]),int(nums[1])))
for x in pairs:
    large = max(x)
    m = (large-1)**2 + 1
    n = 2*(large-1)+1
    if x[0]>=x[1]:
        if large % 2 == 0:
            print(m+n-x[1])
        else:
            print(m+x[1]-1)
    elif x[0]<x[1]:
        if large % 2 == 0:
            print(m+x[0]-1)
        else:
            print(m+n-x[0])


