k = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            ans += gcd(gcd(a,b),c)

print(ans)
