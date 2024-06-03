def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    gcd_seq = [gcd(a[i], a[i + 1]) for i in range(n - 1)]
    
    def is_non_decreasing(seq):
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                return False
        return True
    
    if is_non_decreasing(gcd_seq):
        print("YES")
        continue
    
    found = False
    for i in range(n):
        temp_gcd_seq = []
        if i == 0:
            temp_gcd_seq = [gcd(a[j], a[j + 1]) for j in range(1, n - 1)]
        elif i == n - 1:
            temp_gcd_seq = [gcd(a[j], a[j + 1]) for j in range(n - 2)]
        else:
            for j in range(n - 1):
                if j == i - 1:
                    temp_gcd_seq.append(gcd(a[j], a[j + 2]))
                elif j != i:
                    temp_gcd_seq.append(gcd_seq[j])
        
        if is_non_decreasing(temp_gcd_seq):
            found = True
            break
    
    if found:
        print("YES")
    else:
        print("NO")
