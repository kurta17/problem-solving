import sys

t = int(input())

for _ in range(t):
    n = int(input())
    nums = str(input().strip())
    
    if nums.startswith("2020") or nums.endswith("2020"):
        print("YES")
    elif nums.startswith("2") and nums[1:].endswith("020"):
        print("YES")
    elif nums.startswith("20") and nums[2:].endswith("20"):
        print("YES")
    elif nums.startswith("202") and nums[3:].endswith("0"):
        print("YES")
    else:
        print("NO")


