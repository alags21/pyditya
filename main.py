from math import sqrt
import matplotlib.pyplot as plt

def rect(x):
    if abs(x) > 1:
        return 1
    return 0

def hill(x, a, b):
    new_x = a*x - b
    if abs(new_x) > 1:
        return sqrt(1 - new_x ** 2)
    return 0

xs = [i/250 - 2 for i in range(1000)]

plt.plot(xs, [rect(x) for x in xs])
plt.plot(xs, [hill(x, 1, 0) for x in xs])
