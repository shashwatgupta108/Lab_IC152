import matplotlib.pyplot as plt
import numpy as np


def f(n):
    if n < 2:
        return 1
    else:
        return 1.65 * f(n - 1)


def g(n):
    if n < 2:
        return 1
    else:
        return g(n - 1) + g(n - 2)


def h(n):
    if n < 2:
        return 2
    else:
        return 2 * h(n - 2)


def k(n):
    if n < 3:
        return 3
    else:
        return k(n - 1) + k(n - 3)
