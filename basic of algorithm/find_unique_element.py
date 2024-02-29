def find_unique_element(arr, start, end):
    if start == end:       
        return arr[start]
    
    mid = start + (end - start) // 2

    if mid % 2 == 0:
        if arr[mid] == arr[mid + 1]:
            return find_unique_element(arr, mid + 2, end)
        else:
            return find_unique_element(arr, start, mid)
        
    else:
        if arr[mid] == arr[mid - 1]:
            return find_unique_element(arr, mid + 1, end)
        else:
            return find_unique_element(arr, start, mid - 1)


print(find_unique_element([2,2,3,3,4,4,5,5,6,6,7], 0, 10))  
print(find_unique_element([5,5,10,30,30,40,40,6,6], 0, 8)) 
print(find_unique_element([1,1,2,3,3],0,4)) 
print(find_unique_element([1,2,2,5,5,7,7],0,7))

