a, b, c = map(int, input().split())

if a >= 0 and b >= 0:
    if a > b:
        print(">")
    elif a == b:
        print("=")
    else:
        print("<")

elif a < 0 and b < 0:
    if c % 2 == 1:
        if a > b:
            print(">")
        elif a == b:
            print("=")
        else:
            print("<")
    else:
        if a > b:
            print("<")
        elif a == b:
            print("=")
        else:
            print(">")
            
else:
    if c % 2 == 1:
        if a > b:
            print(">")
        else:
            print("<")
    else:
        k = abs(a)
        p = abs(b)
        if k > p:
            print(">")
        elif k == p:
            print("=")
        else:
            print("<")





