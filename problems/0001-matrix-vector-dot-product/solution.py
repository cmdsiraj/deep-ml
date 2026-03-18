def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	sol = []
	for row in a:
		if len(row) != len(b):
			return -1;
		sum = 0
		for x, y in zip(row, b):
			sum += x*y
		sol.append(sum)

	return sol