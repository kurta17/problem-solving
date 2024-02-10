import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lett = input().strip()
    ans = 0
    lett_dic = dict()

    for i in range(n):
        if lett[i] not in lett_dic:
            ans += 2
            lett_dic[lett[i]] = 1
        else:
            ans += 1
            
    print(ans)


