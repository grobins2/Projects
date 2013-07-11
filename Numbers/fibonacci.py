def f(n, known_values={}):
	if n in known_values:
		return known_values[n]
	if n < 2:
		return n
	else:
		value = f(n-1) + f(n-2)
		known_values[n] = value
	return value