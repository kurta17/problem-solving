# import bisect 
# n = list(map(int, input().split()))
# a,b = map(int, input().split())
# b = n
# n .sort()

# ans = []

# l = bisect.bisect_left(n,a)
# r = bisect.bisect_right(n,b)
# print (l,r)
# for i in range(l,r):
#     ans.append(b[i])


from bisect import bisect_left, bisect_right

def count_points(n, intervals):
    n.sort()

    result = []
    for A, B in intervals:
        left = bisect_left(n, A)
        right = bisect_right(n, B)
        result.append(right - left)

    return result

n = [1, 3, 5, 7, 9]
intervals = [(0, 2), (5, 9), (2, 6)]
print(count_points(n, intervals)) 

# def lowerbound(n,k):
#     ans = None
#     l, r = 0,n
#     mid = l + (r-l) // 2
#     while l < r:
#         if n[l] 