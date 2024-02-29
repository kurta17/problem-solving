import heapq

def k_largest_elements(stream, k):
    min_heap = []
    for num in stream:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
        print(min_heap)
    return min_heap


stream = [10, 20, 11, 70, 50, 40, 100, 5]
k = 3
print(k_largest_elements(stream, k)) 