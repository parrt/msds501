import matplotlib.pyplot as plt
import numpy as np
import random
import time
import math

def minimize(f, x0, eta, h, precision):
    tracex = []
    tracex.append(x0)
    x = x0
    # print str(x0) + " x0"
    while True:
        prev = x
        finite_diff = f(x + h) - f(x)  # /h rolls into learning rate
        x = x - eta * finite_diff  # decelerates x step as it flattens out
        # print "f(%1.12f) = %1.12f" % (x, f(x)),
        tracex.append(x)
        delta = f(x) - f(prev)
        # print ", delta = %1.20f" % delta
        # stop when small change in vertical but not heading down
        if delta >= 0 and abs(delta) < precision: break  # Sometimes subtraction wipes out precision and we get an actual 0.0
    return tracex


if __name__ == '__main__':
    LEARNING_RATE = 50
    h = 0.0001
    PRECISION = 0.0000001  # can't be too small as f(x)-f(xprev) prec is low

    def f(x): return np.exp(-x) * np.cos(2 * np.pi * x)

    a = 0
    b = 5
    graphx = np.arange(a, b, 0.01)
    graphy = f(graphx)
    plt.plot(graphx, graphy)

    random.seed( int(round(time.time() * 1000)) )

    x0s = [.1, 2]

    print "TRIAL 1"
    tracex = minimize(f, x0s[0], LEARNING_RATE, h, PRECISION)
    tracey = [f(x) for x in tracex]
    plt.plot(tracex, tracey, 'ro')
    plt.text(1.5, .85, "f(%1.5f) = %1.9f steps = %d" %
             (tracex[-1], f(tracex[-1]), len(tracex)), fontsize=14,
             color="red")

    print "TRIAL 2"
    tracex = minimize(f, x0s[1], LEARNING_RATE, h, PRECISION)
    tracey = [f(x) for x in tracex]
    plt.plot(tracex, tracey, 'go')
    plt.text(1.5, .75, "f(%1.5f) = %1.9f steps = %d" %
             (tracex[-1], f(tracex[-1]), len(tracex)), fontsize=14,
             color="green")

    plt.savefig('damped-sine-2minima.pdf', format="pdf")

    plt.show()
