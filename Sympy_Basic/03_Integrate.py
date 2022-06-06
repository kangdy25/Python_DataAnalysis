#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:29:06 2022

@author: kangdy25
"""

from sympy import symbols
from sympy import diff
from sympy import sin
from sympy import integrate

x = symbols('x')
f = sin(x)
integrate(f, (x, 0, 3.14))

f = 5 * x
integrate(f, (x, 0, 2))
