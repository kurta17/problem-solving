def mergesort(arr,start,end):
    if end - start < 2:
        return 
    mid = (start + end) // 2
    mergesort(arr,start,mid)
    mergesort(arr, mid, end)
    p1,p2 = start,mid
    res = []
    while p1 < mid and p2 < end:
        if arr[p1] < arr[p2]:
            res.append(arr[p1])
            p1 += 1
        else:
            res.append(arr[p2])
            p2 += 1
    while p1 < mid:
        res.append(arr[p1])
        p1 += 1
    while p2 < end:
        res.append(arr[p2])
        p2 += 1

    for i in range(len(res)):
        arr[start+i] = res[i]
    
    
arr = [2,5,4,3,1]
mergesort(arr,0,5)
print(arr)

    