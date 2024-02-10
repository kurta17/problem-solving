a =  "codeforces"
t = int(input())
for _ in range(t):
    b = str(input())
    result = 0
    for i in range(10):
        if b[i] != a[i]:
            result += 1
    print(result)