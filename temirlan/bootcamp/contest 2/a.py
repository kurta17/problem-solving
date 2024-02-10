# n = int(input())
# pages = list(map(int, input().split()))

# i = 0
# max_page = 0
# count = 0

# while i < n:
#     if pages[i] != i + 1:
#         i += 1
#         if i < n and pages[i] > max_page:
#             max_page = pages[i]
#     elif pages[i] == i + 1 and pages[i] >= max_page:
#         count += 1
#         max_page = 0
#         i += 1
#         if i < n and pages[i] > max_page:
#             max_page = pages[i]
#     else:
#         i += 1

# print(count)

n = int(input())
pages = list(map(int, input().split()))

i = 0
max_page = 0
count = 0

while i < n:
    if pages[i] > max_page:
        max_page = pages[i]
    i += 1

    if i == max_page:
        count += 1
        max_page = 0

print(count)
