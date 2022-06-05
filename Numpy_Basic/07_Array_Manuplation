#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:25:53 2022

@author: kangdy25
"""

import numpy as np
a = np.arange(1, 7, 1)  

b = a.reshape(2, 3)

c = np.linspace(1, 10, 10)

d = np.linspace(1, 10, 10).reshape(2, 5)


x = np.array([[1, 2], [3, 4]])

np.repeat(x, 2, axis=0)
np.repeat(x, 2, axis=1)

np.repeat(x, [1, 2], axis=1)
np.repeat(x, [3, 1], axis=1)


x = np.array([[1], [2], [3]])
y = np.array([[4], [5], [6]])
np.concatenate((x,y), axis=0)
np.concatenate((x,y), axis=1)

x = np.array([10, 20, 30])
y = np.array([40, 50, 60])

np.vstack((x, y))
np.hstack((x, y))

X = np.array([[10., 20., 30.], 
             [40., 50., 60.]])

np.hsplit(X, 3)
np.vsplit(X, 2)


P = np.array([[10, 20, 30], [40, 50, 60]])
P.transpose()
P.ravel()
P.reshape(-1)

P.ravel(order = 'C') # C-style    row-major
P.ravel(order = 'F') # Fortran-style    column-major

P.flatten()

Q = np.array([[1, 2, 3]])
Q.squeeze()


# idea 1

P1 = np.array([1, 2, 3])
Q1 = np.array([4, 5, 6])

P2 = P1[:,np.newaxis]
Q2 = Q1[:,np.newaxis]

np.concatenate((P2, Q2), axis = 0)
R = np.concatenate((P2, Q2), axis = 1)

# idea 2

R = np.vstack((P1, Q1)).transpose()


# Array Copy
x = np.array([10, 20, 30])
y = x
y is x

# shallow
x = np.array([10, 20, 30, 40])
y = x.view()
y is x

id(x)
id(y)

y[0] = 99
x[3] = 999

y = y.reshape((2, 2))
y[0][1] = 7

x

# Deep
x = np.array([10, 20, 30, 40])
y = x.copy()




