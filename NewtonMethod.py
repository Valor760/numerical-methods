import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial 
    at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

def split_and_convert_to_float(data: str) -> list:
	split_data = data.split(' ')
	converted_data = []
	for x in split_data:
		converted_data.append(float(x))
	return converted_data


'''
x1 = np.array([-3.2, -2.1, 0.4, 0.7, 2, 2.5,2.777])
y1 = np.array([10 -2 0 -7 7 0 0])
'''

def showPlot():
    x = split_and_convert_to_float(input("Input x vector(space separated):\n"))
    y = split_and_convert_to_float(input("Input y vector(space separated):\n"))
    # get the divided difference coef
    a_s = divided_diff(x, y)[0, :]
    # evaluate on new data points
    x_new = np.arange(min(x), max(x), .01)
    y_new = newton_poly(a_s, x, x_new)
    plt.plot(x, y, 'ro')
    plt.plot(x_new, y_new, 'b')


plt.figure(figsize=(15,8))
showPlot()
plt.show()
