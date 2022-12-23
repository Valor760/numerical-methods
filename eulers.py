from math import exp
import matplotlib.pyplot as plt

def func_analytic(a:float, b: float, x0:float, t: float) -> float:
	return (a * x0 * exp(a * t)) / (a + b * x0 * (exp(a * t) - 1))


def func(a: float, b: float, x0: float) -> float:
	return a * x0 - b * (x0 ** 2)


def solve_eulers(a: float, b: float, h: float, x0: float, r_end: float):
	t = [0]
	t0 = 0 + h

	# Prepare t array
	while t0 <= r_end:
		t.append(t0)
		t0 += h

	# Calculate values
	arr_analytic = [x0]
	arr_given = [x0]
	arr_error = [0]
	for i in range(1, len(t)):
		arr_analytic.append(arr_analytic[i-1] + h * func_analytic(a, b, arr_analytic[i-1], t[i]))
		arr_given.append(arr_given[i-1] + h * func(a, b, arr_given[i-1]))
		arr_error.append(abs(arr_given[i] - arr_analytic[i]))

	return arr_given, arr_analytic, arr_error, t


def main() -> None:
	a = float(input("Input a: "))
	b = float(input("Input b: "))
	h = float(input("Input h: "))
	x0 = float(input("Input initial condition x0: "))
	r_end = float(input("Input right end: "))

	arr_given, arr_analytic, arr_error, t = solve_eulers(a, b, h, x0, r_end)

	plt.plot(t, arr_analytic, 'b')
	plt.plot(t, arr_given, 'r')
	plt.show()

if __name__ == "__main__":
	main()