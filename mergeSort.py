def mergeSort(givenList):
	"""
	The merge sort algorithm is a classic recursive algorithm that uses a 
	divide and conquer approach. 
	Consists of the steps;
	1. Recursively sort the left half of the input array
	2. Recursively sort the right half of the input array
	3. Merge two sorted sub arrays into one.
	"""

	# Base Case
	if len(givenList) > 1:
		# Splitting array
		middle = len(givenList)//2
		left = givenList[:middle]
		right = givenList[middle:]
		# Recursive calling function for both sub arrays
		mergeSort(left)
		mergeSort(right)

		# Initializes pointers for left; i right; j and result; k
		i = 0
		j = 0
		k = 0

		# Traverse and merge sorted arrays
		while  i < len(left) and j < len(right):
			# if left < right
			if left[i] < right[j]:
				givenList[k] = left[i]
				i += 1
			# Otherwise if right <= left
			else:
				givenList[k] = right[j]
				j += 1
			k += 1

		# Assigment operations
		while i < len(left):
			givenList[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			givenList[k] = right[j]
			j += 1
			k += 1
		return givenList


