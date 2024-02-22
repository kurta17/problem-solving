n = list(map(int, input().split()))
x = int(input())
# # A
# ans = None
# l,r = 0, len(n)-1
# while l <= r:
#     mid = l + (r-l)//2
#     if n[mid] < x:
#         l = mid + 1
#     elif n[mid] > x:
#         ans = n[mid]
#         r = mid - 1
#     else:
#         if mid+1 < len(n):
#             ans = n[mid+1]
#         break

# print(ans)


#B
ans = None
l,r = 0, len(n)-1
while l <= r:
    mid = l + (r-l)//2
    if n[mid] > x:
        r = mid - 1
    elif n[mid] < x:
        ans = n[mid]
        l = mid + 1
    else:
        if mid-1 >= 0:
            ans = n[mid-1]
        break
print(ans)