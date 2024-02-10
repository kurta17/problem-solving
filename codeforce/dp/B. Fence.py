import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h = list(map(int, input().split()))

h_pre = [0] * n  
h_pre[0] = h[0]  

for i in range(1, n):
    h_pre[i] = h_pre[i-1] + h[i]

i = 0
min_height_index = 0
min_height_sum = float('inf')

while i + k <= n:
    current_height_sum = h_pre[i + k - 1] - (h_pre[i - 1] if i > 0 else 0)

    if current_height_sum < min_height_sum:
        min_height_sum = current_height_sum
        min_height_index = i

    i += 1

print(min_height_index + 1)  

    

