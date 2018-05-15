
def bubble_sort(givenList):
	numIterations = len(givenList) - 1
	for i in range(numIterations):
		for j in range(numIterations):
			if givenList[j] > givenList[j+1]:
				temp = givenList[j]
				givenList[j] = givenList[j+1]
				givenList[j+1] = temp

