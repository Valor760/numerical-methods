import numpy as np
import matplotlib.pyplot as plt
from math import exp

a = 0.8
b = 0.1
x0 = 1

def dx_dy_function(t, y):
    return a * y - b * y**2

def analytical_solution(t):
    return (a * x0 * exp(a * t)) / (a + (b * x0 * (exp(a * t) - 1)))


class adamsMethod:
    def __init__(self, t: list, y_0: float, h: float = 0.05):
        self.t = t
        self.y_0 = y_0
        self.h = h

    def get_t_list(self):
        return np.arange(self.t[0], self.t[1] + self.h, self.h)

    def get_y_list(self):
        y_list = [self.y_0]
        t_list = self.get_t_list()
        
        t_x = 0
        for t in t_list:
            if (t_x >= 4):
                y = y_list[-1] + (self.h/24) * ( (55 * dx_dy_function(t, y_list[-1]) )  
                - (59*dx_dy_function(t, y_list[-2])) 
                + (37*dx_dy_function(t, y_list[-3] )) 
                - (9*dx_dy_function(t, y_list[-4])))
                #Yk+1 = Yk + (h/24) * ( (55 * f(Tk, Yk)) 
                # - (59 * f(Tk-1, Yk-1)) 
                # + (37 *f (Tk-2, Yk-2)) 
                # - (9 * f(Tk-3, Yk-3)) )
            else:
                y = y_list[-1] + self.h * dx_dy_function(t, y_list[-1])
            y_list.append(y)
            t_x +=1
            
        return y_list[:-1]

    def get_graph(self):
        t_list = self.get_t_list()
        y_list = self.get_y_list()

        y_2_list = [analytical_solution(t) for t in self.get_t_list()]

        plt.title(f'Solution with h={self.h}')
        plt.plot(t_list, y_list, label='euler_method')
        plt.plot(t_list, y_2_list, 'r', label='analytical_solution', linestyle='dashed')

        plt.legend()
        plt.show()

        error = [abs(i - j) for i, j in zip(y_2_list, y_list)]
        print('Max error:', max(error))

        plt.title(f'Error with h={self.h}')
        plt.plot(t_list[4:], error[4:], label='error')
        plt.legend()
        plt.show()


res = adamsMethod([0,10], 1, 0.01)
res.get_graph() #Show the Graphs