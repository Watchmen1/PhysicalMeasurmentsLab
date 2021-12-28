#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:59:32 2020

@author: watchmen1
"""

from matplotlib import pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('TEK00018.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        
        
        
plt.plot(x,y, marker='o')

x_ticks = np.arange(-0.006, 0.0061, 0.002)
plt.xticks(x_ticks)

plt.title('Absorption Curves of Rubidium Isotopes 85 and 87')

plt.xlabel('Time(ms)')
plt.ylabel('Volts(V)')

plt.savefig("tek00018_test_plot.pdf")

plt.show()

