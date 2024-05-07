import math

a,b,k = map(int, input().split())
list_of_div_a = []
    
for i in range(1, int(math.sqrt(a)+1)):
    if a % i == 0:
        list_of_div_a.append(i)
        if i * i != a:
            list_of_div_a.append(a // i)

list_of_div_b = []

for i in range(1, int(math.sqrt(b)+1)):
    if b % i == 0:
        list_of_div_b.append(i)
        if i * i != b:
            list_of_div_b.append(b // i)

ans = []

for i in list_of_div_b:
    if i in list_of_div_a:
        ans.append(i)

ans.sort(reverse=True)
print(ans)
print(ans[k-1])