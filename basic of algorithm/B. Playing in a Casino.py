t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cards = []

    for _ in range(n):
        a = list(map(int, input().split()))
        cards.append(a)
    
    # Transpose the matrix to get columns
    columns = list(map(list, zip(*cards)))

    total = 0
    for column in columns:
        print(column)

    
