from math import sin


def func(x: float) -> float:
	return sin(2 * x) * x - 17


def solve_bisection(a: float, b: float, E: float) -> None:
	iter = 0

	while True:
		x = (a + b) / 2
		fx = func(x)
		fa = func(a)
		fb = func(b)
		if (fa * fx) <= 0:
			b = x
		else:
			a = x

		delta = abs(a - b)
		print(f"Iteration = {iter+1}\tX = {round(x, 5)}\tdelta = {round(delta, 5)}")
		iter += 1

		if delta <= E:
			return


def main() -> None:
	left_border = float(input("Input left border(a): "))
	right_border = float(input("Input right border(b): "))
	if left_border > right_border:
		print(f"ERROR: Left border cannot be more than right border. Left = {left_border} | Right = {right_border}")
		return
	
	accuracy = float(input("Input requered accuracy: "))
	solve_bisection(left_border, right_border, accuracy)


if __name__ == '__main__':
	main()