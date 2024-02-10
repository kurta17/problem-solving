import sys
input = sys.stdin.readline



def func(n):
    denominations = [100, 20, 10, 5, 1]
    count = 0

    for i in denominations:
        count += n // i
        n %= i

    return count

n = int(input())
result = func(n)
print(result)


