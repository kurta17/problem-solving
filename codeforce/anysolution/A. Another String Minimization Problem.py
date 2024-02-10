t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = [0] * m

    for x in map(int, input().split()):
        x -= 1
        x = min(x, m - 1 - x)
        cnt[x] += 1

    ans = ['B'] * m

    for i in range(m):
        if cnt[i] > 0:
            ans[i] = 'A'
            if cnt[i] > 1:
                ans[m - 1 - i] = 'A'

    print("".join(ans))



