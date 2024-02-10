import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

set_num = set()

answers = [0] * n


for i in range(n - 1, -1, -1):
    set_num.add(nums[i])
    answers[i] = len(set_num)


for _ in range(m):
    l = int(input()) - 1
    print(answers[l])

