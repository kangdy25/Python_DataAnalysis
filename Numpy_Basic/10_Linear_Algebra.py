#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:03:06 2022

@author: kangdy25
"""

import numpy as np

M = np.array([[10, 20], [30, 40]])
N = np.array([[1, 2], [3, 4]])

M * N
M @ N
M.dot(N)

a = np.zeros((3,3))
b = np.ones((3, 3))
c = np.trace(b)

M = np.array([[1., -3.,], [2., 4.]])
y = np.array([[1.], [3.]])

M_inv = np.linalg.inv(M)

x = M_inv @ y

x = np.linalg.solve(M, y)


# singular value decomposition
np.linalg.svd(M)

N = np.zeros((5, 5))
np.fill_diagonal(N, 100)






