import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    i = s.find("11")
    j = s.rfind("00")
    if i != -1 and j != -1 and i < j:
        print("NO")
    else:
        print("YES")
   