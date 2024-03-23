t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    bet = n - 1
    if k % bet == 0:
        ans = (k // bet * n) - 1
    else:
        ans = (k // bet * n) + k % bet 
    print(ans)