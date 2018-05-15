
def unordered_search(givenList, value):
	for index in range(len(givenList)):
		if value == givenList[index]:
			return index
	return None


def ordered_search(givenList, value):
	for index in range(len(givenList)):
		if value == givenList[index]:
			return index
		elif givenList[index] > term:
			return None
	return None
