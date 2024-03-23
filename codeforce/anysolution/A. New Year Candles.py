a,b = map(int, input().split())

ans = a
left = a 

while left >= b:
    ans += left // b
    k = left // b
    nasht = left - k * b
    left = k +  nasht

print(ans)