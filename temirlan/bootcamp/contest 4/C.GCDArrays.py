import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l,r,k = map(int, input().split())
    if l ==r ==1:
        print("NO")
    elif l != 1 and l == r:
        print("YES")
    else:
        odd_num = (r-l+1)-(r//2-(l-1)//2)
        if odd_num <= k:
            print("YES")
        else:
            print("NO")


