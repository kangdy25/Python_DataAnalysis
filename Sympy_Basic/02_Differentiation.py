#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:24:43 2022

@author: kangdy25
"""

from sympy import symbols
from sympy import diff
from sympy import sin

x = symbols('x')

f = x ** 3

df1 = diff(f, x)
df2 = diff(df1, x)
df3 = diff(df2, x)

f = sin(x)
dfSin = diff(f, x)
