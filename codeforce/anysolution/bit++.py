n = int(input())
x = 0
for i in range(n):
    text = str(input())
    if "+" in text:
        x += 1
    elif "-" in text:
        x -= 1
print(x)