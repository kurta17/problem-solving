n = str(input()).strip()

let = set(map(str, n[1:-1].split(", ")))
if len(n) == 2:
    print(0)
else:
    print(len(let))