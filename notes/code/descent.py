import matplotlib.pyplot as plt
import numpy as np
from runif import *
import time


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
    LEARNING_RATE = 10
    h = 0.0001
    PRECISION = 0.0000001  # can't be too small as f(x)-f(xprev) prec is low

    def f(x): return np.cos(3 * np.pi * x) / x

    graphx = np.arange(.1, 1.1, 0.01)
    graphy = f(graphx)
    plt.plot(graphx, graphy)
    plt.axis([0, 1.1, -4, 6])

    setseed(int(round(time.time() * 1000)))

    x0s = [runif(.1, 1.2), runif(.1, 1.2)]  # random starting positions

    print "TRIAL 1"
    tracex = minimize(f, x0s[0], LEARNING_RATE, h, PRECISION)
    tracey = [f(x) for x in tracex]
    plt.rcParams.update({'font.size': 18})
    plt.plot(tracex, tracey, 'ro')
    plt.text(0.3, 4.5, "f(%1.5f) = %1.9f" % (tracex[-1], f(tracex[-1])), fontsize=18,
             color="red")
    plt.text(0.3, 4, "steps=" + str(len(tracex)), fontsize=18, color="red")

    print "TRIAL 2"
    tracex = minimize(f, x0s[1], LEARNING_RATE, h, PRECISION)
    tracey = [f(x) for x in tracex]
    plt.rcParams.update({'font.size': 18})
    plt.plot(tracex, tracey, 'go')
    plt.text(0.3, 3.2, "f(%1.5f) = %1.9f" % (tracex[-1], f(tracex[-1])), fontsize=18,
             color="green")
    plt.text(0.3, 2.8, "steps=" + str(len(tracex)), fontsize=18, color="green")

    #plt.savefig('cos-trace-2minima.pdf', format="pdf")

    plt.show()
