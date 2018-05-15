
def small_change(denom, total_amount):
	sorted_denom = sorted(denom, reverse = True)
	series = []
	for j in range(len(sorted_denom)):
		term = sorted_denom[j:]

		num_denom = []
		local_total = total_amount
		for i in term:
			div = local_total / i
			local_total = local_total % i
			if div > 0:
				num_denom.append((i, div))
		series.append(num_denom)
	return series