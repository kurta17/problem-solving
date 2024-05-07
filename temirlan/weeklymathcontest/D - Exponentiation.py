def fast_exp(a, b):
	P = 10**9 + 7
	if b == 0:
		return 1
	if b == 1:
		return a
	if b % 2 == 1:
		x = fast_exp(a, b - 1)	
		return (x * a) % P
	else:
		x = fast_exp(a, b // 2)
		return (x * x) % P

P = 10^9 + 7
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print(fast_exp(a,b))
