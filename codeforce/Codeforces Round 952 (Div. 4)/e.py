import math

t = int(input())

for _ in range(t):
    x, y, z, k = map(int, input().split())
    ans = 0
    l = int(math.sqrt(k)) + 1
    for a in range(1, l):
        if k % a == 0:
            for b in range(1, int(math.sqrt(k//a)) + 1):
                if (k//a) % b == 0:
                    c = k // (b*a)
                    if a * b * c == k:
                        dimensions = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]
                        for cord_a, cord_b, cord_c in dimensions:
                            if cord_a <= x and cord_b <= y and cord_c <= z:
                                option = (x - cord_a + 1) * (y - cord_b + 1) * (z - cord_c + 1)
                                ans = max(ans, option)
    
    print(ans)
