n_0 = int(input())

prime_nth = []

def find_nth_prime(n_0):
    primes = []
    i = 2
    while len(primes) < n_0:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1
    
    prime_nth.append(primes[-1])
    
find_nth_prime(n_0)
i = 0
while i<3:
    find_nth_prime(prime_nth[-1])
    i+=1

print(prime_nth[-1])


# def find_nth_prime(n_0):
#     if len(prime_nth) == 5:
#         return primes[-1]
#     primes = []
#     i = 2
#     while len(primes) < n_0:
#         for p in primes:
#             if i % p == 0:
#                 break
#         else:
#             primes.append(i)
#         i += 1
#     next_find = primes[-1]
#     prime_nth.append(next_find)
#     return find_nth_prime(next_find)

# print(find_nth_prime(n_0))
