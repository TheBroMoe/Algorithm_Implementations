
def insertion_sort(givenList):
	for index in range(1, len(givenList)):
		searchIndex = index
		insertValue = givenList[index]

		while searchIndex > 0 and givenList[searchIndex - 1] > insertValue:
			givenList[searchIndex] = givenList[searchIndex - 1]
			searchIndex -= 1
		givenList[searchIndex] = insertValue

