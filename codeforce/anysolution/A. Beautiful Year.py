y = int(input())

while True:
    y += 1
    if len(set(str(y))) == 4:
        break

print(y)
