N, W = map(int, input().split())
options = []
total = 0

for _ in range(N):
    c, w = map(int, input().split())
    if w != 0:
        options.append([c / w, c, w])
    else:
        total += c


def merge(x, l, m, r):
    tmp = []
    i1 = l
    i2 = m
    while i1 < m or i2 < r:
        if (i2 >= r) or ((i1 < m) and (x[i1] < x[i2])):
            tmp.append(x[i1])
            i1 += 1
        else:
            tmp.append(x[i2])
            i2 += 1
    x[l:r] = tmp


def merge_sort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if r - l > 1:
        m = (l + r) // 2
        merge_sort(x, l, m)
        merge_sort(x, m, r)
        merge(x, l, m, r)


merge_sort(options, 0, len(options))



for i in reversed(options):
    if W == 0:
        break
    elif i[2] > W:
        total += int(i[1] * (W / i[2]))
        break
    else:
        total += i[1]
        W -= i[2] 

print(total)















# import random


# def partition(x, l, r, pivot):
#     il = l
#     ir = r

#     i = l
#     while i < ir:
#         if x[i] < pivot:
#             x[i], x[il] = x[il], x[i]
#             il += 1
#             i += 1
#         elif x[i] > pivot:
#             ir -= 1
#             x[i], x[ir] = x[ir], x[i]
#         else:
#             i += 1

#     return il, ir


# def qsort(x, l=0, r=None):
#     if r is None:
#         r = len(x)
#     if (r - l) > 1:
#         pivot = x[random.randint(l, r - 1)]
#         il, ir = partition(x, l, r, pivot)
#         qsort(x, l, il)
#         qsort(x, ir, r)


# n, w = map(int, input().split())

# a = []

# ans = 0

# for i in range(n):
#     price, weight = map(int, input().split())
#     if weight != 0:
#         a.append((price / weight, price, weight))
#     else:
#         ans += price

# qsort(a)

# a.reverse()


# for i in range(len(a)):
#     if w == 0:
#         break
#     elif a[i][2] > w:
#         ans += int(a[i][1] * (w / a[i][2]))
#         break
#     else:
#         ans += a[i][1]
#         w -= a[i][2]

# print(ans)
# '