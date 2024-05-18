def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

m = int(input())
count = 0
num = 1

# while count < m:
#     num += 1
#     if is_prime(num):
#         count += 1

print(is_prime(num)) 


