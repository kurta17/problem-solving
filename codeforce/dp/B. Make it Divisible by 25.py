
f = ["00", "25", "50", "75"]

t = int(input())

for _ in range(t):
    n = input().strip()
    
    ans = 100
    for e in f:
        sptr = len(n) - 1
        cur_ans = 0

        while sptr >= 0 and n[sptr] != e[1]:
            sptr -= 1
            cur_ans += 1

        if sptr >= 0:
            sptr -= 1

            while sptr >= 0 and n[sptr] != e[0]:
                sptr -= 1
                cur_ans += 1

            ans = min(ans, cur_ans)

    print(ans)


