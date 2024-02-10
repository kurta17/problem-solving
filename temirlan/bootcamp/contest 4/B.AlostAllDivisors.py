import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    ans = nums[0] * nums[-1]
    divis1 = []
    divis2 = []
    div = 1

    while ans >= div * div:
        if ans % div == 0:
            divis1.append(div)
            if div != ans//div:
                divis2.append(ans//div)
        div +=1
    divis2.reverse()
    divisors = divis1 + divis2
    
    if divisors[1:-1] == nums:
        print(ans)
    else:
        print(-1)  


    
        

    