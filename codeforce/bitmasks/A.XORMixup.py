t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    for i in range(n):
        x = 0
        for j in range(n):
            if i != j:
                x ^= a[j]
        if x == a[i]:
            print(a[i])
            break
