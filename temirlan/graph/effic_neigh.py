n,m = map(int, input().split())
s = int(input())
friends = [[] for _ in range(n+1)]

def binary_search(y,friends_x):
    a = 0
    b = len(friends_x) - 1
    while a <= b:
        mid = (a + b)//2
        if friends_x[mid] > y:
            b = mid - 1
        elif friends_x[mid] < y:
            a = mid + 1
        else:
            return True
    return False

answer = []
    
for _ in range(m):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)


for i in friends:
    i.sort()

for x in friends[s]:
    for y in friends[x]:
        ans = binary_search(y,friends[s])
        if not ans:
            answer.append(y)

print(len(set(answer)))
