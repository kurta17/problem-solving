import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())

    res_1 = 1 if b==c or ((b % 2) ==  (c % 2))  else 0
    res_2 = 1 if a==c or ((a % 2) ==  (c % 2)) else 0
    res_3 = 1 if b==a or ((b % 2) ==  (a % 2)) else 0

    print(res_1,res_2,res_3)
    