t = int(input())

for _ in range(t):
    a = str(input())
    b = str(input())
    ans = True
    k = 0
    i = 0
    while k < len(a) and i < len(b):
        if a[k] != b[i]:
            ans = False
            break
        cnt_a = 1
        cnt_b = 1
        while k < len(a)-1 and a[k] == a[k+1]:
            k += 1
            cnt_a += 1
        while i < len(b)-1 and b[i] == b[i+1]:
            i += 1
            cnt_b += 1
        if cnt_b < cnt_a:
            ans = False
            break
        i +=1
        k +=1

    if k < len(a) or i < len(b):
        ans = False

    print("YES" if ans else "NO")
