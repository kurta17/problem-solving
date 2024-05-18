mod = 10**9 + 7

def generate_divisors(prime_factors):
    divisors = [1]
    
    for prime, power in prime_factors:
        current_divisors = []
        current_powers = [prime ** exp for exp in range(power + 1)]
        
        for d in divisors:
            for cp in current_powers:
                current_divisors.append(d * cp)
                
        divisors = current_divisors
        
    return sorted(divisors)

n = int(input())
num = []
number_n = 1
sum_n = 1

for _ in range(n):
    p,i = list(map(int, input().split())) 

    number_n *= (i+1)
    v = (p ** (i+1) - 1) // (p-1)
    sum_n *= v

    num.append((p,i))

div = generate_divisors(num)
product_n = 1
for d in div:
    product_n *= d
    
print(number_n % mod, sum_n % mod, product_n % mod)