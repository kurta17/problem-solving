n = int(input().strip())

lucky_digits = {'4', '7'}
is_almost_lucky = False

for i in range(1, n + 1):
    if n % i == 0 and all(digit in lucky_digits for digit in str(i)):
        is_almost_lucky = True
        break

if is_almost_lucky:
    print("YES")
else:
    print("NO")


