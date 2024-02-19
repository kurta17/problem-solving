import sys
input = sys.stdin.readline

n,x = map(int,input().split())
num = list(map(int,input().split()))

nums = list(enumerate(num))
nums.sort(key=lambda x: x[1])
ans = True
i = 0
j = n-1

while i < j:        
    if (nums[i][1]+nums[j][1]) == x:
        print(nums[i][0]+1,nums[j][0]+1)
        ans = False
        break
    elif (nums[i][1]+nums[j][1]) > x:
        j -=1
    else:
        i += 1
    

if ans:
    print("IMPOSSIBLE")
    
        
    
    

