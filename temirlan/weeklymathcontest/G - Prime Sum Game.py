def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def optimal_winner(A, B, C, D):
    if max(A, C) <= min(B, D):
        for i in range(max(A, C), min(B, D) + 1):
            if not is_prime(i + C):
                return "Aoki"
        return "Takahashi"
    else:
        return "Aoki"

A, B, C, D = map(int, input().split())
print(optimal_winner(A, B, C, D))
