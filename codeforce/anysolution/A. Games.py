import sys
input = sys.stdin.readline

t = int(input())
home = []
guest = []
for _ in range(t):
    a,b = map(int, input().split())
    home.append(a)
    guest.append(b)

ans = 0

for i in home:
    for g in guest:
        if i == g:
            ans += 1

print(ans)
