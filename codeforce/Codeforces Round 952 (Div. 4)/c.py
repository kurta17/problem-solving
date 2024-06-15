from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    def_dict = defaultdict(int)
    ans = 0
    prefix_sum = a[0]

    if a[0] == 0:
        ans += 1
    def_dict[a[0]] += 1
    
    for i in range(1, n):
        def_dict[a[i]] += 1
        prefix_sum += a[i]
        if prefix_sum % 2 == 0 and def_dict[prefix_sum // 2] > 0:
            ans += 1
            
    print(ans)
