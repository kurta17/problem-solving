n = int(input())

num = [0] * (n + 1)
num[0] = 0
num[1] = 9  

for i in range(2,n+1):
    num[i] = num[i-1] * 8 

print(num[i])


