
def partiion(givenList, start, end):
	pivot, pivotIndex = givenList[start], start
	finalIndex = end
	less_than_pivot_index = finalIndex
	greater_than_pivot_index = start + 1

	while True:
		while givenList[greater_than_pivot_index] < pivot and greater_than_pivot_index < end:
			greater_than_pivot_index += 1
		while givenList[less_than_pivot_index] > pivot and less_than_pivot_index >= start:
			less_than_pivot_index -= 1

		if greater_than_pivot_index < less_than_pivot_index:
			temp = givenList[greater_than_pivot_index]
			givenList[greater_than_pivot_index] = givenList[less_than_pivot_index]
			greater_than_pivot_index[less_than_pivot_index] = temp
		else:
			break
	givenList[pivotIndex] = givenList[less_than_pivot_index]
	givenList[less_than_pivot_index] = pivot
	return less_than_pivot_index

def quick_sort(givenList, start, end):
	if end - start <= 0:
		return
	else:
		partiion_point = partiion(givenList, start, end)
		quick_sort(givenList, first, partiion_point - 1)
		quick_sort(givenList, partiion_point + 1, last)

