#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:57:14 2022

@author: kangdy25
"""

import numpy as np

# number type
a = np.array([10, 20, 30])
a.dtype

a[2] = 30.1
a.dtype
a

a.dtype.Name 
a = a.astype('float64')
a[2] = 30.1
a

b = np.array([10., 20., 30.])

c = np.array([10.1, 20.1, 30.1], 'int32')


# divide by 2
x = np.array([7, 9, 11])
y = x / 2


# int32 VS int64
# int32가 나타낼 수 있는 가장 큰 수 2,147,483,648
# int64가 나타낼 수 있는 가장 큰 수 9,223,372,036,854,775,807

p = np.array([0], 'int32')
p[0] = 2147483647
p[0] = p[0] + 1
 
q = np.array([0], 'int64')
q[0] = 9223372036854775807
q[0] = q[0] + 1










