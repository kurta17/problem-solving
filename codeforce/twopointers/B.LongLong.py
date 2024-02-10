t = int(input())

for _ in range(t):
    n = int(input())
    num_list = list(map(int, input().split()))
    
    total_sum = 0
    count = 0
    check = False

    for i in num_list:
        total_sum += abs(i)
        if i > 0:
            check = False
        if i < 0 and not check:
            check = True
            count +=1

    print(total_sum,count)

    
        
            




        
        

            