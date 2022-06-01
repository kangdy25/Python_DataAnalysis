#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 22:52:27 2022

@author: kangdy25
"""
import numpy as np

# Math and Locial Operation
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

c = a + b
c = a - b
c = b**2
c = 2 * a

idx = b < 20
idx = a < 20

a = a + 1 # a += 1
a = a * 2 # a *= 2

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
np.divide(a, b)
np.divmod(a, b)
np.exp(b)
np.sqrt(b)