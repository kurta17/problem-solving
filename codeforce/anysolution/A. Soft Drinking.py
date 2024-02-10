import sys
input = sys.stdin.readline

n, k, l, c, d, p, nl, np = map(int, input().split())

p_lit = (k * l)// nl
p_lime = (c * d)
p_salt = (p // np)

print(min(p_lime,p_salt,p_lit) // n)

