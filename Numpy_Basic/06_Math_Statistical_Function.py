# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

a = np.array([10, 20, 30])
np.mean(a)
a.mean()

np.average(a)
np.average(a, weights=[1, 1, 1])
np.average(a, weights=[1, 1, 0])
np.average(a, weights=[0, 1, 1])
np.average(a, weights=[1, 0, 1])

np.median(a)

np.cumsum(a)

np.cov(a)

np.std(a)

np.var(a)


# Numpy Useful Function
x = np.array([10, 20, 30])

x.sum()

x = np.array([10., 20., 30., 25., 15.])

x.min() # 최솟값
x.argmin() # 최솟값의 위치

x_min, x_min_idx = x.min(), x.argmin()

x.max()
x_max, x_max_idx = x.max(), x.argmax()

x.ptp()

x.sort()


a = np.array([10, 20, 30])
b = np.array([-5, 25])
np.searchsorted(a, b)




