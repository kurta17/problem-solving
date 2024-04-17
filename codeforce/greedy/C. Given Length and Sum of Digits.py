m, s = map(int, input().split())

if s > 9 * m or s == 0:
    print("-1 -1")

min_num = [0] * m
max_num = [0] * m

for i in range(m):
    if s >= 10:
        max_num[i] = 9
        s -= 9
    else:
        max_num[i] = s
        s = 0
        
for i in range(m - 1, -1, -1):
        if s > 1:
            min_num[i] = min(s - 1, 9)
            s -= min_num[i]
        else:
            min_num[i] = s
            s -= s
    

print(min_num)
print(''.join(map(str, reversed(min_num))), ''.join(map(str, max_num)))