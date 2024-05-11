import math

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

for k in range(1, m + 1):
    is_coprime = True
    
    for num in a:
        if gcd(k, num) != 1:
            is_coprime = False
            break

    if is_coprime:  
        ans.append(k)
    
print(len(ans))
for i in ans:
    print(i)
