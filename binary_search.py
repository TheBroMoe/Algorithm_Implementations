def binary_search(givenList, value):
	listSize = len(givenList) - 1

	first_element_index = 0
	last_element_index = listSize

	while first_element_index <= last_element_index:
		midpoint = (first_element_index + last_element_index) // 2

		if givenList[midpoint] == value:
			return midpoint
		elif givenList[midpoint] < value:
			first_element_index = midpoint + 1
		else:
			last_element_index = midpoint - 1

	if first_element_index > last_element_index:
		return None


def binary_search_recursive(givenList, first_element_index, last_element_index, value):
	if (last_element_index < first_element_index):
		return None
	else:
		midpoint = first_element_index + (last_element_index - first_element_index) //2
		if givenList[midpoint] > value:
			return binary_search_recursive(givenList, first_element_index, midpoint - 1, value)

		elif givenList[midpoint] < value:
			return binary_search_recursive(givenList, midpoint + 1, last_element_index, value)
		else:
			return midpoint

store = [2,4,5,12,43,54,60,77]

print(binary_search(store, 2))
print(binary_search_recursive(store, 0, 7, 2))