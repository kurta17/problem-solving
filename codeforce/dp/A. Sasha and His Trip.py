n,v = map(int, input().split())
tank = v
ans = v
full = n - 1
for i in range(2,n):
    if full == tank:
        break
    else:
        full -= 1
        ans += i
if n <= v:
    print(n-1)
else:
    print(ans)


    

