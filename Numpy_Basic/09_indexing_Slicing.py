#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 13:44:06 2022

@author: kangdy25
"""

import numpy as np

M1 = np.array([100., 101., 102., 103., 104.])
M1[0]
M1[4]
M1[-1]

M1[0:3:1]
M1[:]
M1[::1]
M1[::2]
M1[::-1]
M1[::-2]
M1[-2::-2]


M2 = np.array([[100., 101., 102.], [200., 201., 202.]])

M2[0][0]
M2[0][2]
M2[0, 2]
M2[0, 0]

M2[:,:]
M2[0,:]
M2[1,:]
M2[:,0]

M2[:,[0, 2]]
M2[:, -1]
M2[:, ::-1]


M3 = np.array([
                [[100., 101., 102., 103.], 
                 [104., 105., 106., 107.],
                 [108., 109., 110., 111.]
                ],
                [[200., 201., 202., 203.], 
                 [204., 205., 206., 207.],
                 [208., 209., 210., 211.]]
            ])


M3[0, 0, 0]
M3[0,:,:]
M3[1,:,:]


x = np.array([10., 20., 30.])
idx = np.where(x == 30.)
x[idx]



