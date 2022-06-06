#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:35:34 2022

@author: kangdy25
"""

from sympy import symbols, diff, integrate, limit, Function, Eq, dsolve

t = symbols('t')
x = Function('x')
ODE = Eq(x(t).diff(t,t) + x(t))
dsolve(ODE, x(t))
