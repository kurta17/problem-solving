import sys
input = sys.stdin.readline
t = int(input())
 
for _ in range(t):
    n, h = map(int, input().split())
    d = list(map(int, input().split()))
    d.sort(reverse=True)  
    
    ans = (h // (d[0] + d[1])) * 2  
    
    if h % (d[0] + d[1]) > 0: 
        if h % (d[0] + d[1]) <= d[0]: 
            ans += 1
        else:
            ans += 2
    
    print(ans)

