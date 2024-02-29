# counting sort

def counting_sort(arr):
    if not arr:
        return []

    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create a counting array to store the count of each element
    count = [0] * (max_element + 1)

    # Store the count of each element in the counting array
    for num in arr:
        count[num] += 1

    # Modify the counting array to store the position of each element in the sorted array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create the output array
    output = [0] * len(arr)

    # Place each element at its correct position in the output array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Example usage:
arr = [4, 2, 22, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
