import math


invphi = (math.sqrt(5) - 1) / 2  # 1 / phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1 / phi^2

def gss(f, a, b, acc=1e-5):
    (a, b) = (min(a, b), max(a, b))
    h = b - a
    if h <= acc:
        return (a, b)

    # Required steps to achieve tolerance
    n = int(math.ceil(math.log(acc / h) / math.log(invphi)))

    c = a + invphi2 * h
    d = a + invphi * h
    yc = f(c)
    yd = f(d)
    i = 0
    for k in range(n-1):
        if yc < yd:  # yc > yd to find the maximum
            b = d
            d = c
            yd = yc
            h = invphi * h
            c = a + invphi2 * h
            yc = f(c)
        else:
            a = c
            c = d
            yc = yd
            h = invphi * h
            d = a + invphi * h
            yd = f(d)
        i += 1

    if yc < yd:
        return (a, d, i)
    else:
        return (c, b, i)

f = lambda x: (x / (math.sin(3 *x) ** 2)) + 3 #Function
a = -1 #left border(a):
b = -0.1 #right border(a):
acc = 0.01 #accuracy 
(c, d, i) = gss(f, a, b, acc)
print(c, d, i)