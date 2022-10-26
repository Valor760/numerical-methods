from math import sqrt


def split_and_convert_to_float(data: str) -> list:
	split_data = data.split(' ')
	converted_data = []
	for x in split_data:
		converted_data.append(float(x))
	return converted_data


def main() -> None:
	print("Input array of coefficients(space separated separated")
	coefficients = input()
	coefficients = split_and_convert_to_float(coefficients)
	
	n = sqrt(len(coefficients))
	if n != round(n):
		print("Matrix is not NxN size!")
		print(f"Your matrix: [{coefficients}]")
		return

	


if __name__ == '__main__':
	main()