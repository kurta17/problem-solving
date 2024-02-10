import sys
input = sys.stdin.readline

t = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8]
chars = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(t):
    a = input().strip() 
    c, n = a[0], int(a[1])  

    for num in nums:
        if num == n:
            continue
        else:
            print(c + str(num))

    for char in chars:
        if char == c:
            continue
        else:
            print(char + str(n))


