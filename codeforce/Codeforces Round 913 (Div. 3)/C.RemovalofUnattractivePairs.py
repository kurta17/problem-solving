t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    # Count adjacent pairs of different characters
    count = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            count += 1

    # Minimum length after removal
    result = count // 2
    print(result)


