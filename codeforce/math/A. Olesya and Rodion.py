n, t = map(int, input().split())

if t == 2:
    ans = "2" * (n) 
    print(ans)
elif t == 4:
    ans = "4" * (n)
    print(ans) 
elif t == 8:
    ans = "8" * (n)
    print(ans) 
elif t == 6:
    ans = "6" * n
    print(ans)
elif t == 3:
    ans = "3" * (n)
    print(ans) 
elif t == 5:
    ans = "5"* (n)
    print(ans)
elif n>1 and t == 10:
    ans = "1" * (n-1) + "0"
    print(ans)
elif t == 9:
    ans = "9" * n
    print(ans)
elif t == 7:
    ans = "7" * n
    print(ans)
else:
    print(-1)
 
