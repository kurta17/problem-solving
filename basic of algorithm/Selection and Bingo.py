# 2. Selection Sort and Bingo Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Function to print the Array
def printArray(arr):
	print("Sorted Array: ",end="")
	for ele in arr:
		print(ele, end=" ")
	print()

# function for Sorting the Array
def bingoSort(arr, size):

	# Finding the smallest element From the Array
	bingo = min(arr)
	# Finding the largest element from the Array
	largest = max(arr) 
	nextBingo = largest
	nextPos = 0
	while bingo < nextBingo:
		# Will keep the track of the element position to
		# shifted to their correct position
		startPos = nextPos
		for i in range(startPos, size):
			if arr[i] == bingo:
				arr[i], arr[nextPos] = arr[nextPos], arr[i]
				nextPos += 1
			# Here we are finding the next Bingo Element
			# for the next pass
			elif arr[i] < nextBingo:
				nextBingo = arr[i]
				
		bingo = nextBingo
		nextBingo = largest
	
	# Printing the ELements of the Sorted Array
	printArray(arr) 
		
arr = [ 5, 4, 8, 5, 4, 8, 5, 4, 4, 4 ]
bingoSort(arr, size = len(arr))

arr2 = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
bingoSort(arr2, size = len(arr2)) 

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array using Selection Sort:", arr)





