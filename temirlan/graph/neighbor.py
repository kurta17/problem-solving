n,m = map(int, input().split())
s = int(input())
pairs = []


    
for _ in range(m):
    a,b = map(int, input().split())
    pairs.append((a,b))

def get_neighbors(node):
    neig = []

    for (a,b) in pairs:
        if a == node:
            neig.append(b)
        elif b == node:
            neig.append(a)
    return neig

N_s = get_neighbors(s)
ans = []
for x in N_s:
    N_x = get_neighbors(x)
    for y in N_x:
        if y not in N_s:
            ans.append(y)
        
print(len(set(ans)))





    