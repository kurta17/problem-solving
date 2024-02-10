def min_moves_to_increase_array(n, arr):
    moves = 0
    prev = arr[0]
    
    for i in range(1, n):
        if arr[i] < prev:
            moves += prev - arr[i]
        else:
            prev = arr[i]
    
    return moves

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
result = min_moves_to_increase_array(n, arr)
print(result)


# def my_func(a, b):
#     cout = 0
#     for i in range(1,a):
#         while b[i-1] > b[i]:
#             b[i] += 1
#             cout += 1
#     print(cout)
        
# a = int(input())
# b = list(map(int, input().split()))

# my_func(a, b)


# a = int(input())
# b = list(map(int,(input().split())))

# cout = 0
# for i in range(1,a):
#     while b[i-1] > b[i]:
#         b[i] += 1
#         cout += 1
# print(cout)
    
