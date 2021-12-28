#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:59:45 2020

@author: watchmen1
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('Theta vs Magnetic Field Strength Exp3 - Sheet1.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[1]))
        y.append(float(row[0]))
        
x = np.array(x)
y = np.array(y)        
        
plt.scatter(x,y, marker='o')
m, b = np.polyfit(x, y, 1)

plt.plot(x, float(m)*x + float(b), 'r')
# x_ticks = np.arange(-0.010, 0.011, 0.002)
# plt.xticks(x_ticks)

plt.title('Theta vs Magnetic Field Strength(B)')

plt.xlabel('Magnetic Field Strength (milliTesla)')
plt.ylabel('Theta(radians)')

plt.savefig("exp3_theta_vs_B_plot.pdf")

plt.show()