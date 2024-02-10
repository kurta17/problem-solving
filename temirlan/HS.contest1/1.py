n = input()
answer = 0
open = []
close = []

for m in range(len(n) - 1):
    if n[m] == n[m + 1] and n[m] == "(":
        open.append((m, m + 1))
    elif n[m] == n[m + 1] and n[m] == ")":
        close.append((m, m + 1))
print(open)
print(close)
for a in open:
    for b in close:
        if a[0] < b[0]:
            answer += 1

print(answer)
