
def selection_sort(givenList):
	listSize = len(givenList)

	for i in range(listSize):
		for j in range(i+1, listSize):
			if givenList[j] < givenList[i]:
				temp = givenList[i]
				givenList[i] = givenList[j]
				givenList[j] = temp

