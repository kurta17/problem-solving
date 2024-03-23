t = int(input())
 
for _ in range(t):
    n = int(input())
    if n == 2:
        print("YES")
        print("AA")
    elif n % 2 == 0:
        print("YES")
        print("BAA" * (n // 2))
    else:
        print("NO")


