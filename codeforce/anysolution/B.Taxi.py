n = int(input())
s = list(map(int, input().split()))

count = [0]*5
for i in range(n):
    count[s[i]] += 1

taxi = count[4] + count[3] + count[2]//2
count[1] -= count[3]
if count[2] % 2 == 1:
    taxi += 1
    count[1] -= 2

if count[1] > 0:
    taxi += (count[1] + 3) // 4

print(taxi)
