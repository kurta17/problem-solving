t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split())) 

    same1 = 1
    same2 = 1

    for i in range(n-1):
        if nums[i] == nums[i+1]:
            same1 += 1
        else:
            break

    for i in range(n-1,0,-1):
        if nums[i] == nums[i-1]:
            same2 += 1
        else:
            break


    if nums[0] != nums[-1]:
        print(n-(max(same1, same2)))
    else:
        a = n-(same1+same2)
        if a >0:
            print(a)
        else:
            print(0)



