a = list(map(str,input().split("+")))
a.sort()

if len(a) == 1:
    print("".join(a))
else:
    b = "+".join(a)
    print(b)
 