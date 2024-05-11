def fast_exp(a, b):
	P = 10**9 + 7
	ans = 1

	while b > 0:
		if b % 2 == 1:
			ans = (ans * a) % P
		a = (a * a) % P
		b //= 2
		
	return ans

P = 10^9 + 7
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print(fast_exp(a,b))
