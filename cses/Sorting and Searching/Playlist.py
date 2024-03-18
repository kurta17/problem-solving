n = int(input())
songs = list(map(int, input().split()))

k = set()
i = 0
j = 0
ans = 0

while i < n:
    print(k)
    if songs[i] not in k:
        k.add(songs[i])
        ans = max(ans, len(k))
        i += 1
        print(k)
    else:
        k.remove(songs[j])
        j += 1
        

print(ans) 