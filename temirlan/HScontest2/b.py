t = int(input())

for i in range(t):
    n , k = map(int, input().split())
    integlist = list(map(int, input().split()))
    

    odd_num = 0
    for x in integlist:
        if x % 2 == 1:
            odd_num += 1
    
    if odd_num < k or (odd_num - k) % 2 == 1:
        print("NO")
    else:
        print("YES")
        segments = 0
        for i in range(k - 1):
            while integlist[segments] % 2 == 0:
                segments += 1
            print(segments + 1, end=" ")
            segments += 1
        print(n)
       
