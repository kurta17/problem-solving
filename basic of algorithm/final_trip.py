from typing import List

def max_trips(A: List[int], B: List[int]) -> int:
    trips = sorted(zip(A, B), key=lambda trip: trip[1])
    print(trips)
    last_end = -1
    max_trips = 0

    for i in trips:
        if i[0] > last_end:
            max_trips += 1
            last_end = i[1]

    return max_trips

print(max_trips([1, 2, 3, 4], [5, 6, 7, 8]))
print(max_trips([2, 7, 8, 9], [3, 9, 10, 10]))

