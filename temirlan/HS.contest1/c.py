
n, m, p = map(int, input().split())

like = []
annoying = []

for i in range(n):
    a, b = map(int, input().split())
    like.append(a)
    annoying.append(b)
for i in like:
    for x in annoying:
        if i != x and i > p:
            answer = i - p
        
if sorted(like) == sorted(annoying):
    answer = -1

print(answer)



