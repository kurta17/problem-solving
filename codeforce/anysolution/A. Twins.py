n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
value = sum(coins) // 2
i = 0
ind = 0
while i <= value: 
    i += coins[ind]
    ind += 1

print(ind)



