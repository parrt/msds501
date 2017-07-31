import matplotlib.pyplot as plt
import numpy as np
import random
import time


def minimize(f, x0, eta, h, precision):
    x = x0
    while True:
        prev = x
        finite_diff = f(x + h) - f(x)  # /h rolls into learning rate
        x = x - eta * finite_diff  # decelerates x step as it flattens out
        # print "f(%1.12f) = %1.12f delta = %1.20f" % (x, f(x), f(x) - f(prev))
        if abs(x - prev) < precision:
            return x

def minimize_trace(f, x0, eta, h, precision):
    tracex = [x0]
    x = x0
    while True:
        prev = x
        finite_diff = f(x + h) - f(x)  # /h rolls into learning rate
        x = x - eta * finite_diff  # decelerates x step as it flattens out
        tracex.append(x)
        if abs(x - prev) < precision:
            return tracex

def viz_trace(x0):
    # Plot the damped sine curve
    graphx = np.arange(.1, 1.3, 0.01)
    graphy = [f(x) for x in graphx] # or just f(graphx)!
    plt.plot(graphx, graphy)

    random.seed(int(round(time.time() * 1000)))

    tracex = minimize_trace(f, x0, ETA, h, PRECISION)
    tracey = [f(x) for x in tracex]
    plt.scatter(tracex, tracey, color="green", marker='o')
    plt.text(0.3, 4.5, "f(x=%1.5f) = %1.9f, steps = %d" %
             (tracex[-1], f(tracex[-1]), len(tracex)), fontsize=14,
             color="green")
    plt.show()

if __name__ == '__main__':
    ETA = 10
    h = 0.0001
    PRECISION = 0.0000001  # can't be too small as f(x)-f(xprev) prec is low

    def f(x): return np.cos(3 * np.pi * x) / x

    x0 = random.uniform(.1, 1.2)
    viz_trace(x0)

    # Or can just call to get x
    x0 = random.uniform(.1, 1.2)
    minx = minimize(f, x0, ETA, h, PRECISION)
    print "f(%f) = %f" % (minx, f(minx))

    plt.show()
