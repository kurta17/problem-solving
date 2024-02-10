t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = [i for i in range(1, n + 1)]

    if n == 1:
        print("-1")
        continue

    for i in range(n - 1):
        if A[i] == B[i]:
            B[i], B[i + 1] = B[i + 1], B[i]

    if A[n - 1] == B[n - 1]:
        B[n - 1], B[n - 2] = B[n - 2], B[n - 1]

    print(" ".join(map(str, B)))


