import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    cnt1 = 0
    cnt2 = 0
    for i in w:
        if i == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    if (cnt1 + 2 * cnt2) % 2 != 0:
        print("NO")
    else:
        total_sum = (cnt1 + 2 * cnt2) // 2
        if total_sum % 2 == 0 or (total_sum % 2 == 1 and cnt1 != 0):
            print("YES")
        else:
            print("NO")