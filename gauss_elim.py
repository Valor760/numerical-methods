from math import sqrt


def solve_gauss_elim(A: list, B: list, n: int) -> list:
	curr_col_idx = 0
	lead_row_idx = 0

	for i in range(n): # i - column
		# Find leading row index
		nums = []
		for j in range(0, n): # j - row
			nums.append(abs(A[j][i])) # Add absolute value of each row in column
		lead_row_idx = nums.index(max(nums))

		# Place leading row on the first place (don't forget to swap in B vec)
		A[0], A[lead_row_idx] = A[lead_row_idx], A[0] 
		B[0], B[lead_row_idx] = B[lead_row_idx], B[0]
		lead_row_idx = 0

		# Divide leading row by leading value
		div_val = A[lead_row_idx][i]
		for j in range(n): # j - column
			A[lead_row_idx][j] /= div_val
		B[lead_row_idx] /= div_val

		# Eliminate rows
		for j in range(n): # j - row
			if j != lead_row_idx:
				for k in range(n): # k - column
					A[j][k] = A[j][k] - A[lead_row_idx][k] * A[j][i]
				B[j] = B[j] - B[lead_row_idx] * A[j][i]


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
	vecA = input("Input A vector(space separated separated):\n")
	vecA = split_and_convert_to_float(vecA)
	
	n = sqrt(len(vecA))
	if n != round(n):
		print("Matrix is not NxN size!")
		print(f"Your matrix: [{vecA}]")
		return
	n = int(n)
	matA = convert_to_matrix(vecA, n)

	vecB = input("Input B vector:\n")
	vecB = split_and_convert_to_float(vecB)
	if len(vecB) != n:
		print("Vector B length is not equal to A matrix length!")
		print(f"Vector B length: {len(vecB)}   Matrix A length: {n}")
		return

	solve_gauss_elim(matA, vecB, n)
	print(f"Mat A:\n{matA}")
	print(f"Vec B: {vecB}")	


if __name__ == '__main__':
	main()