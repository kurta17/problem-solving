t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print(0)
    elif min(set(a)) < n:
        print(4)


        
