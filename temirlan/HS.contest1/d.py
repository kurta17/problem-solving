H, W = map(int, input().split())
N = int(input())

A = list(map(int, input().split()))

colors = []
for i in range(N):
    colors.extend([i + 1] * A[i])

table = [[0] * W for _ in range(H)]

i = 0
for r in range(H):
    for c in range(W):
        if r % 2 == 0:
            table[r][c] = colors[i]
        else:
            table[r][W - c - 1] = colors[i]
        i += 1

for row in table:
    print(*row)