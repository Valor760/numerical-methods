from math import sqrt
import time
import matplotlib.pyplot as plt


def get_points_x(left:float, right: float, h: float = 0.01) -> list:
	interval_values = []
	n_left = left
	while n_left <= right:
		interval_values.append(n_left)
		n_left += h
	return interval_values


def generate_plot_data(min: float, max: float, coeffs: list) -> list:
	points = []
	interval_values = get_points_x(min, max)

	for x in interval_values:
		value = 0
		for i in range(len(coeffs)):
			value += coeffs[i] * (x ** i)
		points.append(value)

	return points


def solve_lsq(X: list, Y:list, n: int, k: int) -> list:
	# Fill matrix A
	matA = []
	for i in range(k):
		matA.append([1] * k)

	for i in range(k):
		for j in range(k):
			buff = []
			for idx in range(n):
				buff.append(X[idx] ** (i + j))
			matA[i][j] = sum(buff)
	
	# Fill matrix B
	matB = [sum(Y)]
	for power in range(1, k):
		buff = []
		for idx in range(n):
			buff.append((X[idx] ** power) * Y[idx])
		matB.append(sum(buff))

	solve_gauss_elim(matA, matB, k)
	return matB


def solve_gauss_elim(A: list, B: list, n: int) -> list:
	lead_row_idx = 0

	for i in range(n): # i - column
		# Find leading row index
		nums = []
		for j in range(i, n): # j - row
			nums.append(abs(A[j][i])) # Add absolute value of each row in column
		lead_row_idx = nums.index(max(nums)) + i

		# Place leading row on the ith place (don't forget to swap in B vec)
		A[i], A[lead_row_idx] = A[lead_row_idx], A[i] 
		B[i], B[lead_row_idx] = B[lead_row_idx], B[i]
		lead_row_idx = i

		# Divide leading row by leading value
		div_val = A[lead_row_idx][i]
		for j in range(n): # j - column
			A[lead_row_idx][j] /= div_val
		B[lead_row_idx] /= div_val

		# Eliminate rows
		for j in range(n): # j - row
			if j != lead_row_idx:
				x = A[j][i]
				for k in range(n): # k - column
					A[j][k] = A[j][k] - A[lead_row_idx][k] * x
				B[j] = B[j] - B[lead_row_idx] * x


def split_and_convert_to_float(data: str) -> list:
	split_data = data.split(' ')
	converted_data = []
	for x in split_data:
		converted_data.append(float(x))
	return converted_data


def main() -> None:
	size_n = int(input("Input size N: "))

	vecX = split_and_convert_to_float(input("Input vector X(space separated):\n"))
	if len(vecX) != size_n:
		print(f"ERROR: vector X size != N: X length - {len(vecX)} | N - {size_n}")
		return

	vecY = split_and_convert_to_float(input("Input vector Y(space separated):\n"))
	if len(vecY) != size_n:
		print(f"ERROR: vector Y size != N: Y length - {len(vecY)} | N - {size_n}")
		return

	k = int(input("Input K order: "))
	if k < 0:
		print(f"ERROR: Order K couldn't be less than 0! Your value = {k}")
		return
	else: k+=1

	# Solve equation
	start = time.time()
	result = solve_lsq(vecX, vecY, size_n, k)
	duration = time.time() - start


	print(f"\nAnswer is: {[round(x, 4) for x in result]}")
	print(f"Time: {round(duration * 1000, 2)}ms")	

	points = generate_plot_data(min(vecX), max(vecX), result)
	plt.plot(vecX, vecY, 'bo')
	plt.plot(get_points_x(min(vecX), max(vecX)), points)
	plt.show()

if __name__ == '__main__':
	main()
	input("Press any key to continue...")