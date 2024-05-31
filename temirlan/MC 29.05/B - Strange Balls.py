n = int(input())
a = list(map(int, input().split()))

ans = 0
count = 0
stack = []

for x in a:
    ans += 1
    if len(stack) > 0 and stack[-1][0] == x:
        stack[-1][1] += 1
        if stack[-1][1] == stack[-1][0]:
            ans -= stack[-1][0]
            stack.pop()
            count += 1
    else:
        stack.append([x, 1])
    print(ans)
    


# n = int(input())
# a = list(map(int, input().split()))


# count = 1
# balls = 1

# for i in range(n-1):
#     print(balls)
#     if a[i] == a[i+1] and a[i] != count:
#         count += 1
#         balls += 1
#     elif a[i] == count:
#         balls -= count - 1
#         count = 1
#     else:
#         count = 1
#         balls += 1
    
# print(balls)

