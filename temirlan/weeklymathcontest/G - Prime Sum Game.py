import math

x = 201

# Initialize is_prime correctly
is_prime = [True] * (2 * x)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(2 * x)) + 1):
    if is_prime[i]:
        for j in range(i * i, 2 * x, i):
            is_prime[j] = False

A, B, C, D = map(int, input().split())

ans = True

for i in range(A, B+1):
    good = True
    for k in range(C, D+1):
        if is_prime[i + k]:
            good = False
            break
    if good:
        ans = False
        

if ans:
    print("Aoki")
else:
    print("Takahashi")
