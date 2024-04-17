n = int(input())
laptops = sorted([list(map(int, input().split())) for _ in range(n)])

for i in range(1, n):
    if laptops[i][1] < laptops[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")