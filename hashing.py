def hashing(myS):
	multiplier = 1
	hashVar = 0
	for char in myS:
		hashVar += multiplier * ord(char)
		multiplier += 1
	return hashVar

