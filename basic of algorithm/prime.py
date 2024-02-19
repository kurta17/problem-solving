# import math
# def findprime(x):
#     for i in range(2,int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

n = int(input())

# if findprime(n):
#     print("YES")
# else:
#     print("NO")

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, n):
        if primes[p]:
            prime_numbers.append(p)
    return prime_numbers

print(sieve_of_eratosthenes(n))