n = int(input())
table = dict()

for i in range(n):
    name = input()
    if name in table:
        table[name] += 1
    else:
        table[name] = 1

students = sorted(table.items(), key=lambda x: (-x[1], x[0]))
for s in students:
    print(s[0], s[1])
