#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:21:04 2022

@author: kangdy25
"""

from sympy import symbols

x = symbols('x')

expr = 2 * x
expr.subs(x, 0)
expr.subs(x, 2)
