import sys

input = sys.stdin.readline

n = int(input())
names_count = {}

for _ in range(n):
    name = str(input()).strip()

    if name in names_count:
        names_count[name] += 1
        ans = name + str(names_count[name])
        print(ans)
    else:
        names_count[name] = 0
        print("OK")


