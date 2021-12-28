#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:34:28 2020

@author: watchmen1
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('far_rot_exp1_data1.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        
# print(y)

# plt.figure()
# plt.scatter(x, y)
# plt.show()

from scipy import optimize

# x_array = np.radians(np.array(x)) 
# x_array = np.array(x) 
y_array = np.array(y) 

def test_func(x_data, a ,b) :
    return a * np.cos(np.radians(2.59) - b * np.radians(x_data)) ** 2 

# params, params_covariance = optimize.curve_fit(test_func, x_array, y_array, bounds=(0, [0.5, 1.]))
params, params_covariance = optimize.curve_fit(test_func, x_array, y_array)
print(params)

plt.figure()
plt.scatter(x_array, y_array, label='Data')
plt.plot(x_array, test_func(x_array, 0.301, params[1]), label='Fitted function: 0.301 x Cos^2(2.59 - 0.989 * theta)')
plt.legend(loc='best')
plt.title('Faraday Rotation Experiment 1')
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity (milli-Volts)')
plt.savefig("far_rot_exp1_test_plot.pdf")
plt.show()
