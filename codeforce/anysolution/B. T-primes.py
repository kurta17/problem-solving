def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    for i in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

def generate_t_primes(primes):
    t_primes = set()
    for p in primes:
        t_primes.add(p*p)
    return t_primes

def main():
    limit = 10**12
    primes = sieve_of_eratosthenes(int(limit**0.5) + 1)
    t_primes = generate_t_primes(primes)

    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] in t_primes:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

