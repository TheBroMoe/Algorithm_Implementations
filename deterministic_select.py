
def partition(givenList, first, last):

	if first == last:
		return first
	else:
		nearestMedian = median_of_medians([first:last])

		index_of_nearest_median = get_index_of_nearest_median(givenList, first, last, nearestMedian)

		swap(givenList, first, index_of_nearest_median)

		pivot = givenList[first]
		pivotIndex = first
		index_of_last_element = last

		less_than_pivot_index = index_of_last_element
		greater_than_pivot_index = first + 1


def median_of_medians(elems):
	sublists = [elems[j:j+5] for j in range(0,len(elems),5)]

	medians = []
	for sublist in sublists:
		medians.append(sorted(sublist)[len(sublist)//2])

	if len(medians) <= 5:
		return sorted(medians)[len(medians)//2]
	else:
		return median_of_medians(medians)

def get_index_of_nearest_median(givenList, first, second, median):
	if first == second:
		return first
	else:
		return first + givenList[first:second].index(median)

def swap(givenList, first, second):
	temp = givenList[first]
	givenList[first] = givenList[second]
	givenList[second] = temp

def deterministic_select(givenList, left, right, k):
	split = partition(givenList, left, right, k):
	if split == k:
		return givenList[split]
	elif split <k:
		return deterministic_select(givenList, split + 1, right, k)
	else:
		return deterministic_select(givenList, left, split - 1, k)