from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a_dict = defaultdict(int)
    ans = 0
    for i in range(n):
        dif = a[i] - (i+1)
        if dif in a_dict:
            ans += a_dict[dif]
            a_dict[dif] += 1
        else:
            a_dict[dif] = 1
    
    print(ans)