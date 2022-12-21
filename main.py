import math



class GSS:
    def __init__(self, interval: list, eps: float = 0.01):
        self.interval = interval
        self.eps = eps

    @staticmethod
    def f(x: float):
        # return x * math.exp(x / 2)  # FUNCTION
        return math.sin(2 * x) * x - 17

    def get_solution(self):
        for i in range(len(self.interval) - 1):
            a = self.interval[i]
            b = self.interval[i + 1]

            if not self.f(a) * self.f(b) <= 0:  # Check for existance
                continue

            x = None
            i = 1
        while abs(b - a) > self.eps:
            if abs(self.f(a)) > abs(self.f(b)):
                x = a + 0.618 * abs(b - a)
            else:
                x = a + 0.382 * abs(b - a)

            aBefore = a
            bBefore = b

            if self.f(a) * self.f(x) <= 0:
                b = x
            else:
                a = x
            print(f'Iteration: {i}, x = {round(x, 4)} , with value a = {round(aBefore, 4)} and b = {round(bBefore, 4)}')
            i += 1
        return x


print(GSS([18, 18.2, 18.4, 18.6, 18.8, 19, 19.2, 19.4, 19.6, 19.8, 20], 0.01).get_solution())
