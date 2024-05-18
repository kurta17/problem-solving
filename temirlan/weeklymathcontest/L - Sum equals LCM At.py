n = 10 ** 9
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] =is_prime[2] = False
small_primes = []

def sieve(n):
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        if is_prime[i]:
            small_primes.append(i)

sieve(n)

def large_prime(n,small_prime):
    if n < small_prime[-1]:
        return n in small_prime
    for i in small_prime:
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

t = int(input())
print(small_primes)
for _ in range(t):
    num = int(input())

    if large_prime(num,small_primes):
        print("No")
    else:
        print("Yes")