n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()
pairs = 0
i, j = 0, 0

while i < n and j < m:
    if abs(boys[i] - girls[j]) <= 1:
        pairs += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1
        
print(pairs)

# dp_boys = [0] * (k)
# dp_girls = [0] * (l)

# for i in boys:
#     dp_boys[i-1] += 1
#     dp_boys[i] += 1
#     dp_boys[i+1] += 1

# for i in girls:
#     dp_girls[i-1] += 1
#     dp_girls[i] += 1
#     dp_girls[i+1] += 1

# p1 = 0
# p2 = 0
# ans = 0

# while p1 < k or p2 < l:
#     if abs(dp_boys[p1] - dp_girls[p2]) <= 1:
#         ans += 1


# print(dp_boys)
# print(dp_girls)
