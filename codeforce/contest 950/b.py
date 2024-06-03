import bisect
t = int(input())

for _ in range(t):
    n,f,k = map(int, input().split())
    a = list(map(int, input().split()))

    fav = a[f-1]
    a.sort(reverse=True)
    a = [-1*val for val in a]
    pos_l = bisect.bisect_left(a, (-1) * fav) 
    pos_r = bisect.bisect_right(a, (-1) * fav)
    
    if pos_r - 1 < k:
        print("YES")
    elif pos_l >= k:
        print("NO")
    else:
        print("MAYBE")

