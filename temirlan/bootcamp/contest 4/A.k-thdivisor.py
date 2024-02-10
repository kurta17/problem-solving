import sys
input = sys.stdin.readline

n,k = map(int, input().split())
divis1 = []
divis2 = []
div = 1

while n >= div * div:
    if n % div == 0:
        divis1.append(div)
        if div != n//div:
            divis2.append(n//div)
    div +=1
divis2.reverse()
divisors = divis1 + divis2

if len(divisors)> k -1:
    print(divisors[k-1])
else:
    print(-1)
    