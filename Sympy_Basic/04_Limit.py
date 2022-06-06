#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:32:50 2022

@author: kangdy25
"""

from sympy import symbols
from sympy import diff
from sympy import sin
from sympy import integrate
from sympy import limit

x = symbols('x')
limit(sin(x)/x, x, 0)
