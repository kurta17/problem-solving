t= int(input())
for _ in range(t):
    n = int(input())
    if n <= 28:
        num = n - 2 + 96
        let = chr(num)
        print("aa"+ let)
    elif n> 27 and n<= 53:
        num = n - 27 + 96
        let_mid = chr(num)
        print("a" + let_mid +"z")
    else:
        num = n - 52 + 96
        let_fir = chr(num)
        print(let_fir +"zz")

