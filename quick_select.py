from quick_sort import partition

def quick_select.py(givenList, left, right, k):
	split = partition(givenList, left, right)

	if split == k:
		return givenList[split]
	elif split < k:
		return quick_select(givenList, split + 1, right, k)
	else:
		return quick_select(givenList, left, split - 1, k)