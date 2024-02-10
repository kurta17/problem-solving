
a, b = map(int, input().split())


if 1 <= a <= 100 and 1 <= b <= 100:
    if a == 1 or b == 1:
        result = a + b
    else:
        result = a * b
    print(result)

# result = max(a+b,a*b)
# print(result)