x = int(input())

b_x = bin(x)
ans = 0
for i in b_x:
    if i == "1":
        ans+=1

print(ans)