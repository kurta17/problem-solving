import sys
input = sys.stdin.readline

n = int(input())
movies = []

for _ in range(n):
    a, b = map(int, input().split())
    movies.append((b, a))  

movies.sort() 
last_end = 0
ans = 0

for end, start in movies:
    if start >= last_end:  
        ans += 1
        last_end = end  

print(ans)