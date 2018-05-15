
def calcMidpoint(givenList, lower, upper, value):
	return lower + ((upper - lower) // (givenList[upper] - givenList[lower])) * (value - givenList[lower])

def interpolation_search(givenList, value):
	listSize = len(givenList) - 1

	lower = 0
	upper = listSize

	while lower <= upper:
		midpoint = calcMidpoint(givenList, lower, upper, value)

		if midpoint > upper or midpoint < lower:
			return None
		elif givenList[midpoint] == value:
			return midpoint
		elif givenList[midpoint] < value:
			lower = midpoint + 1
		else:
			lower = midpoint - 1
	if lower > upper:
		return None

