import sys
input = sys.stdin.readline

a = str(input()).strip()
count = 1
c_max = 1
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        count += 1
    else:
        c_max = max(c_max,count)
        count = 1
c_max = max(c_max,count)
if c_max >= 7:
    print("YES")
else:
    print("NO")