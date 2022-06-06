#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 13:38:39 2022

@author: kangdy25
"""

import numpy as np

a = np.array([0, 1, 2])

a.all()

a.any()

a.nonzero()

np.where(a>0)

a = np.array([0, 10, 20])
np.where(a == 0)
