n = int(input())
last = n % 4

if last == 1:
    print(8)
elif last == 2:
    print(4)
elif last == 3:
    print(2)
elif n == 0:
    print(1)
else:
    print(6)
    