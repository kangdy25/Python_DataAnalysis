# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

# insert
a = np.array([10, 20, 30])
a = np.insert(a, 0, 5)

# delete
a = np.delete(a, 0)
a

# Array Generation Functions
a = np.array([1, 2, 3])
a
a = np.arange(3)
a
a = np.zeros((2, 3))
a
a = np.ones((2, 3))
a
a = np.linspace(0, 5, 6)
a
a = np.logspace(0, 5, 11)
a