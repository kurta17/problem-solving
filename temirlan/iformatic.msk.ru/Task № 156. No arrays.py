n = int(input()) - 1
nums = list(map(int, input().split()))
ans = []

def rever(ans,nums,n):
    if n < 0:
        print(" ".join(map(str, ans)))
        return
    else:
        ans.append(nums[n])
        rever(ans, nums,n-1)

rever(ans,nums,n)

