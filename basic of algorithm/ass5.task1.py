def mergesort(arr,start,end):
    if end - start < 2:
        return 
    mid = (start + end) // 2
    mergesort(arr,start,mid)
    mergesort( arr, mid, end)
    p1,p2 = start,mid
    ans = 0
    
    
    
arr = [2,5,4,3,1]
mergesort(arr,0,5)
print(arr)