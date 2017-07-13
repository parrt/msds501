from descent import minimize
import numpy as np
import sys

"""
Results should look like:

x0 = 0.10; min = cosf(x=0.297)=-3.172
x0 = 0.80; min = cosf(x=0.989)=-1.006
x0 = 0.30; min = cosf(x=0.297)=-3.172
x0 = 1.20; min = cosf(x=0.989)=-1.006
x0 = 0.05; min = cosf(x=0.297)=-3.172
x0 = 2.00; min = x2(x=2.000)=1.000
x0 = -1.00; min = x2(x=2.000)=1.000
x0 = -9.30; min = x2(x=2.000)=1.000
x0 = 2.00; min = x3(x=0.333)=-0.593
x0 = 0.50; min = x3(x=0.333)=-0.593
x0 = 0.33; min = x3(x=0.333)=-0.593
x0 = 1.00; min = x3(x=0.333)=-0.593
"""


def assertequals(which, result, expecting):
    if abs(result - expecting) > 0.0001:
        sys.stderr.write(
            "Failure: %s expecting %1.4f found %1.4f (not within %1.2f)\n" % (
            which, expecting, result, PRECISION))
        return False
    return True


LEARNING_RATE = 2.0
h = 0.00001
PRECISION = 0.00000001  # can't be too small as f(x)-f(xprev) prec is low


def cosf(x): return np.cos(3 * np.pi * x) / x


def x2(x): return (x - 2) ** 2 + 1


def x3(x): return 5 * x ** 3 + 2 * x ** 2 - 3 * x

def check(f, x0, minx):
    tracex = minimize(f, x0, LEARNING_RATE, h, PRECISION)

    start = tracex[0]
    stop = tracex[-1]

    assert round(stop*10000) == round(minx*10000)

def test_1(): check(cosf, 0.1, 0.29691298)
def test_2(): check(cosf, 0.8, 0.98865134)
def test_3(): check(cosf, 0.3, 0.29691298)
def test_4(): check(cosf, 1.2, 0.98865134)
def test_5(): check(cosf, 0.05, 0.29691298)

def test_6(): check(x2, 2.0, 2.0)
def test_7(): check(x2, -1.0, 2.0)
def test_8(): check(x2, -9.3, 2.0)

def test_9(): check(x3, 2.0, 1 / 3.0)
def test_10(): check(x3, 0.5, 1 / 3.0)
def test_11(): check(x3, 1 / 3.0, 1 / 3.0)
def test_12(): check(x3, 1.0, 1 / 3.0)


# print """def cosf(x): return np.cos(3 * np.pi * x) / x
# def x2(x): return (x-2)**2 + 1
# def x3(x): return 5*x**3 + 2*x**2 - 3*x
# """