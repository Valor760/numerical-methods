from math import sqrt
import time


def matrices_multiply(X: list, Y: list) -> list:
	height = len(X)
	width = len(Y) if len(Y) / height > 1 else 1
	result = []


	# Prepare new matrix
	if width > 1:
		for _ in range(width):
			result.append([])
	
	for i in range(height):
		sum = 0
		for j in range(width):
			if width > 1:
				sum += X[i][j] * Y[j][i]
				result[i].append(sum)
			else:
				sum += X[i][j] * Y[j]
				result.append(sum)
	
	return result



def solve_iterative(A: list, B: list, X0: list, n: int, accurracy: float) -> None:
	# Apply X coefficients on B vector and null the ones in A matrix
	for i in range(n):
		B[i] = B[i] / A[i][i]
		A[i][i] = 0

	k = 0
	while True:
		k += 1
		alfa_x0 = matrices_multiply(A, X0)
		x1 = [alfa_x0[i] + B[i] for i in range(n)]
		delta = max([abs(x1[i] - X0[i]) for i in range(n)])
		X0 = x1

		print(f"K = {k}   Delta = {delta} X1 = {x1}\n")

		if delta <= accurracy: break




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
	# solve_gauss_elim(matA, vecB, n)
	duration = time.time() - start

	# print(f"\nAnswer is: {[round(x, 4) for x in vecB]}")
	print(f"Time: {round(duration * 1000, 2)}ms")	


if __name__ == '__main__':
	main()
	input("Press any key to continue...")