import math
from random import randint

def karatsuba(num01,num02):
	'''
	The karatsuba algorithm  is a multiplication algorithm that 
	is an improvement over the quadratic algorithm and performs at most n**1.585 single digit multiplications.
	it does that by recursively carrying out multiplication operations on progressively smaller inputs.
	'''
	
	# Base Case
	if num01 < 10 or num02 < 10:
		return num01*num02
	
	# N represents the number of digits in the higher input number
	N = max(int(math.log10(num01) + 1), int(math.log10(num02) + 1))
	
	# Rounds up N / 2
	N_Half = int(math.ceil(N / 2.0))
	
	# Adds 1 if n is odd
	N = N if N % 2 == 0 else N + 1
	
	# Splits the input numbers
	a, b = divmod(num01, 10**N_Half)
	c, d = divmod(num02, 10**N_Half)
	
	# Multiply a and c
	ac = karatsuba(a,c)
	
	# Multiply b and d 
	bd = karatsuba(b,d)
	
	# Multiply their sums and subtract ac and bd
	ad_bc = karatsuba((a + b),(c + d)) - ac - bd
	
	# Return product
	return (((10**N)*ac) + bd + ((10**N_Half)*(ad_bc)))

def testKaratsuba():
	'''
	Test function that verifies the function works
	'''
	
	for i in range(1000):
		num01 = randint(1, 10**5)
		num02 = randint(1, 10**5)
		
		expected = num01 * num02
		result = karatsuba(num01,num02)
		if result != expected:
			return "failed"
	return('verified')


print(testKaratsuba())