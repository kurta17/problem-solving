import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = str(input().strip())

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + (ord(s[i - 1]) - 96)

for _ in range(q):
    l, r = map(int, input().split())
    ans = prefix_sum[r] - prefix_sum[l - 1]

    print(ans)
