import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    notes = list(map(int, input().split()))

    dist_notes = set()
    ans = 0
    

    for note in notes:
        if note not in dist_notes:
            dist_notes.add(note)
            ans += 1
        elif note + 1 not in dist_notes:
            dist_notes.add(note + 1)
            ans += 1

    print(ans)

        

