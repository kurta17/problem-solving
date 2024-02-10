num = int(input())
full_arr = []


for i in range(num):
    pair = (input())
    nums = pair.split()
    full_arr.append((int(nums[0]),int(nums[1]), int(nums[2])))
for x in full_arr:
    if x[0] > x[1]:
        print(x[0])
    elif x[0] < x[1] and x[0] + x[2] >= x[1]:
        print(x[1])
    elif x[0] < x[1] and x[0] + x[2] < x[1]:
        print(x[1]+(x[1]- x[0]-x[2]))