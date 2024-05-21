from tqdm import tqdm
s = input()
 
n = int(len(s))
p = 5003
mod = (2 ** 50) - 2
power = [1] * (n + 1)

for i in range(1, n):
    power[i] = (power[i - 1] * p) % mod

h = [0] * (n + 1)
for i in range(n):
    h[i + 1] = (h[i] + (ord(s[i]) - ord('a') + 1) * power[i]) % mod

answer = 0

for l in tqdm(range(1, n + 1)):
    unique = set()
    for i in range(n - l + 1):
        pre = (h[l + i] + mod - h[i]) % mod
        pre = (pre * power[n - i - 1]) % mod
        unique.add(pre)
    answer += len(unique)

print(answer)
