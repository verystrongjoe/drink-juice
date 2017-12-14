"""
Sharp Ratio also considers risk free rate of return (Or called William Sharp)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import  scipy.optimize as spo

def error(line, data) :
    """
    Compute error between given line model and observed data.
    :param line: tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept
    :param data: 2D array where each row is a point(x,y)
    :return:  error as a single real value
    """
    err = np.sum((data[:, 1] - ( line[0]) * data[:,0] + line[1]) **2)
    return err

def test_run() :
    # Define original line
    l_orig = np.float32([4,2])
    print("Original line : C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))
    Xorig = np.linspace(0,10,21)
    Yorig = l_orig[0] * Xorig + l_orig[1]

    plt.plot(Xorig, Yorig, )


def f(X) :
    """
    Given a scalar X, return some value(a real number)
    :param X:
    :return:
    """
    Y = (X - 1.5)**2 + 0.5
    print("X={}, Y={}".format(X,Y))
    return Y

def test_get_minima() :
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp':True})
    print("Minima found at: ")
    print("X=  {}, Y= {}".format(min_result.x, min_result.fun))

    # Plot function values, mark minima
    Xplot = np.linspace(0.5,2.5,21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title("Minima of an objective function")
    plt.show()

if __name__ == "__main__" :
    test_run()