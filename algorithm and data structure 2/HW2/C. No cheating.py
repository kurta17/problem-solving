def check(mid, seats, M):
    count = 1
    last = seats[0]
    for i in range(1, len(seats)):
        if seats[i] - last >= mid:
            last = seats[i]
            count += 1
            if count == M:
                return True
    return False

def max_min_distance(N, M, seats):
    seats.sort()
    left, right = 0, seats[-1] - seats[0]
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid, seats, M):
            left = mid
        else:
            right = mid
    return left


N, M = map(int, input().split())
seats = list(map(int, input().split()))
print(max_min_distance(N, M, seats))