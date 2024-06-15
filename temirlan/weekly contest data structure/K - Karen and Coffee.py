n,k,q = map(int, input().split())   
m_temp = 200000
temp_count = [0]*(m_temp + 2)

for i in range(n):
    l,r = map(int, input().split())
    temp_count[l] += 1
    temp_count[r+1] -= 1

for i in range(1, m_temp + 2):
    temp_count[i] += temp_count[i-1]

is_good = [0]*(m_temp + 2)
for i in range(1, m_temp + 2):
    if temp_count[i] >= k:
        is_good[i] = 1
    
prefix_good = [0]*(m_temp + 2)
for i in range(1, m_temp + 2):
    prefix_good[i] = prefix_good[i-1] + is_good[i]

for i in range(q):
    a,b = map(int, input().split())
    print(prefix_good[b] - prefix_good[a-1])

