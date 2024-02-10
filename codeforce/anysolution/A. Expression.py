a = int(input())
b = int(input())
c = int(input())

ans = a + b + c
ans1 = max(ans,(a+b)*c)
ans2 = max(ans,(c+b)*a)
ans3 = max(ans,(a*b)*c)


print(max(ans1,ans2,ans3))
