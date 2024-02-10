import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    max_pos = nums.index(max(nums))
    min_pos = nums.index(min(nums))
    
    result = min(
        max(max_pos, min_pos) + 1,
        (n - 1) - min(max_pos, min_pos) + 1,
        (n - 1) - max_pos + min_pos + 2,
        (n - 1) - min_pos + max_pos + 2
    )
    
    print(result)

