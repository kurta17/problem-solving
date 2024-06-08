n = int(input())
d = {}
for _ in range(n):
    old, new = input().split()
    if old not in d.values():
        d[old] = new
    else:
        for key, value in d.items():
            if value == old:
                d[key] = new
                break

print(len(d))
for k,v in d.items():
    print(k,v)