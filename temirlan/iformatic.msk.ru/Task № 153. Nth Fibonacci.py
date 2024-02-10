n = int(input())
first = 0
second = 1

def fibon(first, second, iter, n):
    if iter == n:
        return first + second
    else:
        return fibon(second, first + second, iter + 1, n)

print(fibon(0, 1, 2, n))