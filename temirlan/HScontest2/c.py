MOD = 998244353

def power(base, exponent):
    result = base ** exponent
    return result

   

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
D = list(map(int, input().split()))

result = 1


X = 1
for i in range(N):
    X = (X * power(A[i], B[i])) % MOD
# print(X)
Y = 1
for i in range(M):
    Y = (Y * power(C[i], D[i])) % MOD
# print(Y)




myX = {}
myY = {}
j = 0

for i in range(N):
    myX[A[i]] = B[j]
    j +=1

y = 0
for i in range(M):
    myY[C[i]] = D[y] 
    y+=1

# print(myX)
# print(myY)

count = 0
for x in myX.keys():
    if x in myY.keys():
        count += myX[x] - myY[x]
    else:
        count += 1

if X % Y == 0:
    print((2 ** count) % MOD)
else:
    print(0)
        

        

