import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dct ={1:0, 2: 0}

for x in nums:
    if x == 1:
        dct[1] +=1
    else:
        dct[2] +=1
        
if dct[1] == 0 or dct[2]==0:
    print(" ".join(map(str, nums)))
else:
    ans = [2,1]
    twos = [2] * (dct[2]-1)
    ones = [1] * (dct[1]-1)
    result = ans + twos + ones 
    print(" ".join(map(str, result)))