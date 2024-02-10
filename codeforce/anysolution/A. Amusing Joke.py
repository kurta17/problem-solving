a = str(input())
b = str(input())
c = str(input())

old = a + b
m = "".join(sorted(old))
n = "".join(sorted(c))
if m == n:
    print("YES")
else:
    print("NO")