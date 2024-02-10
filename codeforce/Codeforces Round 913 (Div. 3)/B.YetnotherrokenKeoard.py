import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    u, l = [], []

    for i in range(len(s)):
        if s[i] not in ("b", "B"):
            if s[i].isupper():
                u.append((s[i], i))
            else:
                l.append((s[i], i))
        elif s[i] == "b" and l:
            l.pop()
        elif s[i] == "B" and u:
            u.pop()

    ans = sorted(l + u, key=lambda x: x[1])
    
    result = ''.join(char for char, _ in ans)

    print(result)

