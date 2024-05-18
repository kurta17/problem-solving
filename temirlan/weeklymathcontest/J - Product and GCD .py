def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while (n % i) == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1 if n not in factors else factors[n] + 1
    return factors

def max_gcd(N, P):
    if P == 1:
        return 1
    
    factors = prime_factors(P)
    gcd_result = 1
    
    for prime, exponent in factors.items():
        gcd_result *= prime ** (exponent // N)
    
    return gcd_result


N, P = map(int, input().split())

print(max_gcd(N, P))
