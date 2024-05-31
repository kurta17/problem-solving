mod = 998244353

N = int(input().strip())

result = 0
s = 1
length = len(str(N))

for d in range(1, length + 1):
    if d < length:
        end = 10**d - 1
    else:
        end = N
    
    r_length = end - s + 1
    sum_s_e = ((s + end) * r_length // 2) % mod
    

    c = (r_length * (s - 1)) % mod
    result = (result + (sum_s_e - c) % mod) % mod
    
    s = end + 1

print(result)
