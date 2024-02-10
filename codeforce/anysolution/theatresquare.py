# n, m, a = map(int, input().split())

# if n % a == 0 and m % a == 0:
#     print((m * n) // (a * a))
# elif n % a != 0 and m % a == 0:
#     k = n // a + 1
#     l = m // a
#     print(k * l)
# elif n % a == 0 and m % a != 0:
#     k = n // a
#     l = m // a + 1
#     print(k * l)
# elif n % a != 0 and m % a != 0:
#     k = n // a + 1
#     l = m // a + 1
#     print(k * l)

n, m, a = map(int, input().split())

k = (n + a - 1) // a
l = (m + a - 1) // a

result = k * l

print(result)
