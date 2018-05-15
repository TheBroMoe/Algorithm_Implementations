def fib_TopDown(n, memo):
	if n <= 2:
		memo[n] = 1
	if memo[n] is None:
		memo[n] = fib_TopDown(n-1, memo) + fib_TopDown(n-2, memo)
	return memo[n]

def fib_BottomUp(n):
	table = [1,1]

	for i in range(2,n):
		table.append(table[i-1] + table[i-2])
	return table[n]