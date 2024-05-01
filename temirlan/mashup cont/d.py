P = int(input())

n_coins = [1000000000 for _ in range(P+1)]
n_coins[0] = 0
n_coins[1] = 1

fact = [0] * 11

for i in range(1,11):
    coin = 1
    for k in range(1,i+1):
        coin *= k
    fact[i] = coin

for i in range(2, P+1):
    for j in range(1, 11):
        if fact[j] <= i:
            n_coins[i] = min(n_coins[i], 1 + n_coins[i - fact[j]])


 
print(n_coins[P])