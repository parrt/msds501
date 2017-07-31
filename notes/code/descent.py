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
        delta = f(x) - f(prev)
        print "f(%1.12f) = %1.12f delta = %1.20f" % (x, f(x), delta)
        # stop when small change in vertical but not heading down
        if delta >= 0 and abs(delta) < precision:
            return x
    return tracex

def minimize_trace(f, x0, eta, h, precision):
    tracex = [x0]
    x = x0
    while True:
        prev = x
        finite_diff = f(x + h) - f(x)  # /h rolls into learning rate
        x = x - eta * finite_diff  # decelerates x step as it flattens out
        tracex.append(x)
        delta = f(x) - f(prev)
        if delta >= 0 and abs(delta) < precision:
            return tracex

if __name__ == '__main__':
    LEARNING_RATE = 10
    h = 0.0001
    PRECISION = 0.0000001  # can't be too small as f(x)-f(xprev) prec is low

    def f(x): return np.cos(3 * np.pi * x) / x

    graphx = np.arange(.1, 1.3, 0.01)
    graphy = f(graphx)
    plt.plot(graphx, graphy)

    random.seed(int(round(time.time() * 1000)))

    x0s = [random.uniform(.1, 1.2), random.uniform(.1, 1.2)]  # random starting positions

    print "TRIAL 1"
    tracex = minimize_trace(f, x0s[0], LEARNING_RATE, h, PRECISION)
    tracey = [f(x) for x in tracex]
    plt.rcParams.update({'font.size': 14})
    plt.plot(tracex, tracey, 'ro')
    plt.text(0.3, 4.5, "f(%1.5f) = %1.9f steps = %d" %
             (tracex[-1], f(tracex[-1]), len(tracex)), fontsize=14,
             color="red")

    print "TRIAL 2"
    tracex = minimize_trace(f, x0s[1], LEARNING_RATE, h, PRECISION)
    tracey = [f(x) for x in tracex]
    plt.rcParams.update({'font.size': 14})
    plt.plot(tracex, tracey, 'go')
    plt.text(0.3, 3.9, "f(%1.5f) = %1.9f steps = %d" %
             (tracex[-1], f(tracex[-1]), len(tracex)), fontsize=14,
             color="green")

    #plt.savefig('cos-trace-2minima.pdf', format="pdf")

    ETA = 10
    h = 0.0001
    PRECISION = 0.0000001
    x0 = random.uniform(.1, 1.2)
    minx = minimize(f, x0, ETA, h, PRECISION)
    print "f(%f) = %f" % (minx, f(minx))

    plt.show()
