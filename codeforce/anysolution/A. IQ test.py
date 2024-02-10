n = int(input())
nums = list(map(int,input().split())) 
odd = 0
even = 0
ind_odd = 0
ind_even = 0
i = 0
while i < n:
    if nums[i] % 2 ==0:
        even += 1
        ind_even = i
        i +=1
    else:
        odd += 1
        ind_odd = i
        i +=1

if odd == 1:
    print(ind_odd + 1)
else:
    print(ind_even + 1)
    
