def two_power(n):
    if n == 1:
        return 2
    func = two_power(n-1)
    func *= 2
    return func

print(two_power(5))