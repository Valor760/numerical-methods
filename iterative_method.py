from math import sqrt
import time


# This function works only if Y is one-dimensional array
# Since it is used only for multiplying A with X0 - its okay
def matrices_multiply(X: list, Y: list) -> list:
	result = []
	for i in range(len(X)):
		sum = 0
		for j in range(len(Y)):
			sum += X[i][j] * Y[j]
		result.append(sum)

	return result


def solve_iterative(A: list, B: list, X0: list, n: int, accurracy: float) -> None:
	# Apply X coefficients on B vector and null the ones in A matrix
	for i in range(n): 
		div_val = A[i][i]
		B[i] = B[i] / div_val
		for j in range(n): A[i][j] /= -div_val # Divide all values in the row and reverse their sign
		A[i][i] = 0

	k = 0
	last_delta = 0
	while True:
		k += 1
		alfa_x0 = matrices_multiply(A, X0)
		x1 = [alfa_x0[i] + B[i] for i in range(n)]
		delta = max([abs(x1[i] - X0[i]) for i in range(n)])
		X0 = x1

		print(f"K = {k}\tDelta = {round(delta, 6)}\tX1 = {[round(x, 5) for x in x1]}\n")

		if delta <= accurracy or (k >= 10 and last_delta < delta): break
		last_delta = delta


def convert_to_matrix(A: list, n: int) -> list:
	new_arr = []
	sub_arr = []
	for i in range(0, n*n):
		sub_arr.append(A[i])

		if (i+1) % n == 0:
			new_arr.append(sub_arr)
			sub_arr = []
	
	return new_arr	


def split_and_convert_to_float(data: str) -> list:
	split_data = data.split(' ')
	converted_data = []
	for x in split_data:
		converted_data.append(float(x))
	return converted_data


def main() -> None:
	vecA = split_and_convert_to_float(input("Input A vector(space separated):\n"))
	
	# Check vector A is NxN size
	n = sqrt(len(vecA))
	if n != round(n):
		print("Matrix is not NxN size!")
		print(f"Your matrix: [{vecA}]")
		return
	n = int(n) # sqrt returns float...
	matA = convert_to_matrix(vecA, n)

	vecB = split_and_convert_to_float(input("Input B vector(space separated):\n"))
	if len(vecB) != n:
		print("Vector B length is not equal to A matrix length!")
		print(f"Vector B length: {len(vecB)}   Matrix A length: {n}")
		return
	
	vecX0 = split_and_convert_to_float(input("Input X0 vector(space separated):\n"))
	if len(vecX0) != n:
		print("Vector X0 length is not equal to A matrix length!")
		print(f"Vector X0 length: {len(vecX0)}   Matrix A length: {n}")
		return

	accurracy = float(input("Input required accurracy: "))

	# Solve equation
	start = time.time()
	solve_iterative(matA, vecB, vecX0, n, accurracy)
	duration = time.time() - start
	print(f"Time: {round(duration * 1000, 2)}ms")	


if __name__ == '__main__':
	main()
	input("Press any key to continue...")