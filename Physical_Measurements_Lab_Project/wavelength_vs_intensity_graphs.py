#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:10:53 2020

@author: watchmen1
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df350 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/350data1.txt', sep='\t')
df400 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/400data1.txt', sep='\t')
df450 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/450data1.txt', sep='\t')
df500 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/500data1.txt', sep='\t')
df550 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/550data1.txt', sep='\t')
df600 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/600data1.txt', sep='\t')
df650 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/650data1.txt', sep='\t')
df700 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/700data1.txt', sep='\t')

df_corr = pd.read_excel(r'/Users/watchmen1/Python_Projects/Physical_Measurements_Lab_Project/correction_values.xlsx')

wl350 = np.array(df350.iloc[0:3646,0])
intensity350 = np.array(df350.iloc[0:3646,1])

wl400 = np.array(df400.iloc[0:3646,0])
intensity400 = np.array(df400.iloc[0:3646,1])

wl450 = np.array(df450.iloc[0:3646,0])
intensity450 = np.array(df450.iloc[0:3646,1])

wl500 = np.array(df500.iloc[0:3646,0])
intensity500 = np.array(df500.iloc[0:3646,1])

wl550 = np.array(df550.iloc[0:3646,0])
intensity550 = np.array(df550.iloc[0:3646,1])

wl600 = np.array(df600.iloc[0:3646,0])
intensity600 = np.array(df600.iloc[0:3646,1])

wl650 = np.array(df650.iloc[0:3646,0])
intensity650 = np.array(df650.iloc[0:3646,1])

wl700 = np.array(df700.iloc[0:3646,0])
intensity700 = np.array(df700.iloc[0:3646,1])

correction_vals = np.array(df_corr.iloc[0:3646,0])


### 350 wavelength vs intensity graph
new_int350 = intensity350 * correction_vals
#int300plus = new_int350
nint350 = pd.DataFrame(data=np.transpose(np.array([wl350, new_int350])))
nint350 = nint350.rename(columns={ 0 : "wavelength", 1: "intensity"})
nint350 = nint350.astype(float)
plus300 = nint350.loc[nint350['wavelength'] >= 300]

wl350new = plus300.iloc[:,0]
nint350new = plus300.iloc[:,1]

plt.figure(1)
plt.plot(wl350new, nint350new)
# plt.yscale('log')
plt.title('Wavelength vs Intensity 350nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
#ticks = plt.xticks(np.arange(0,len(wl350new),step=800))
plt.savefig('350_with_corr_new.pdf')

### 400 wavelength vs intensity graph
new_int400 = intensity400 * correction_vals

plt.figure(2)
plt.plot(wl400, intensity400)
plt.title('Wavelength vs Intensity 400nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
ticks = plt.xticks(np.arange(0,len(wl400),step=800))
plt.savefig('400_no_corr.pdf')

### 450 wavelength vs intensity graph
new_int450 = intensity450 * correction_vals

plt.figure(3)
plt.plot(wl450, intensity450)
# plt.yscale('log')
plt.title('Wavelength vs Intensity 450nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
ticks = plt.xticks(np.arange(0,len(wl450),step=800))
plt.savefig('450_no_corr.pdf')

### 500 wavelength vs intensity graph
new_int500 = intensity500 * correction_vals

plt.figure(4)
plt.plot(wl500, intensity500)
# plt.yscale('log')
plt.title('Wavelength vs Intensity 500nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
ticks = plt.xticks(np.arange(0,len(wl500),step=800))
plt.savefig('500_no_corr.pdf')

### 550 wavelength vs intensity graph
new_int550 = intensity550 * correction_vals

plt.figure(5)
plt.plot(wl550, intensity550)
# plt.yscale('log')
plt.title('Wavelength vs Intensity 550nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
ticks = plt.xticks(np.arange(0,len(wl550),step=800))
plt.savefig('550_no_corr.pdf')

### 600 wavelength vs intensity graph
new_int600 = intensity600 * correction_vals

plt.figure(6)
plt.plot(wl600, intensity600)
# plt.yscale('log')
plt.title('Wavelength vs Intensity 600nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
ticks = plt.xticks(np.arange(0,len(wl600),step=800))
plt.savefig('600_no_corr.pdf')

### 650 wavelength vs intensity graph
new_int650 = intensity650 * correction_vals

plt.figure(7)
plt.plot(wl650, intensity650)
# plt.yscale('log')
plt.title('Wavelength vs Intensity 650nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
ticks = plt.xticks(np.arange(0,len(wl650),step=800))
plt.savefig('650_no_corr.pdf')

### 700 wavelength vs intensity graph
new_int700 = intensity700 * correction_vals

plt.figure(8)
plt.plot(wl700, intensity700)
# plt.yscale('log')
plt.title('Wavelength vs Intensity 700nm peak')
plt.xlabel('Wavelength (nanometers)')
plt.ylabel('Intensity (counts/second)')
ticks = plt.xticks(np.arange(0,len(wl700),step=800))
plt.savefig('700_no_corr.pdf')



###integration experimenting
wl350new = wl350.astype('float64')

total_array = np.multiply(wl350new, new_int350)
total = np.sum(total_array)

### 350 measurements for average height of peak and 50% peak intensity width

re350 = df350.rename(columns={"179.08": "wavelength", "1205.64": "intensity"})
re350.drop(re350.tail(1).index,inplace=True)
re350 =  re350.astype(float)
half_max350 = re350.loc[(re350["intensity"] >= 3958) & (re350["intensity"] <= 3964)]
vals350 = re350.loc[(re350["wavelength"] >= 345) & (re350['wavelength'] <= 354)]


### 400 measurements for average height of peak and 50% peak intensity width
re400 = df400.rename(columns={"179.08": "wavelength", "1183.73": "intensity"})
re400.drop(re400.tail(1).index,inplace=True)
re400 =  re400.astype(float)
vals400 = re400.loc[(re400["wavelength"] >= 395) & (re400['wavelength'] <= 405)]


### 450 measurements for average height of peak and 50% peak intensity width
re450 = df450.rename(columns={"179.08": "wavelength", "1191.71": "intensity"})
re450.drop(re450.tail(1).index,inplace=True)
re450 =  re450.astype(float)
vals450 = re450.loc[(re450["wavelength"] >= 445) & (re450['wavelength'] <= 454)]


### 500 measurements for average height of peak and 50% peak intensity width
re500 = df500.rename(columns={"179.08": "wavelength", "1200.52": "intensity"})
re500.drop(re500.tail(1).index,inplace=True)
re500 =  re500.astype(float)
vals500 = re500.loc[(re500["wavelength"] >= 490) & (re500['wavelength'] <= 515)]


### 550 measurements for average height of peak and 50% peak intensity width
re550 = df550.rename(columns={"179.08": "wavelength", "1206.66": "intensity"})
re550.drop(re550.tail(1).index,inplace=True)
re550 =  re550.astype(float)
vals550 = re550.loc[(re550["wavelength"] >= 545) & (re550['wavelength'] <= 565)]


### 600 measurements for average height of peak and 50% peak intensity width
re600 = df600.rename(columns={"179.08": "wavelength", "1232.47": "intensity"})
re600.drop(re600.tail(1).index,inplace=True)
re600 =  re600.astype(float)
vals600 = re600.loc[(re600["wavelength"] >= 595) & (re600['wavelength'] <= 610)]


### 650 measurements for average height of peak and 50% peak intensity width
re650 = df650.rename(columns={"179.08": "wavelength", "1186.18": "intensity"})
re650.drop(re650.tail(1).index,inplace=True)
re650 =  re650.astype(float)
vals650 = re650.loc[(re650["wavelength"] >= 645) & (re650['wavelength'] <= 664)]


### 700 measurements for average height of peak and 50% peak intensity width
re700 = df700.rename(columns={"179.08": "wavelength", "1214.86": "intensity"})
re700.drop(re700.tail(1).index,inplace=True)
re700 =  re700.astype(float)
vals700 = re700.loc[(re700["wavelength"] >= 680) & (re700['wavelength'] <= 715)]

wavelengths = [350, 400, 450, 500, 550, 600, 650, 700]
width_est = np.array([363.27 - 341.55, 412.68 - 391.23, 462.87 - 441.5, 511.54 - 490.28, 561.42 - 541.88, 611.99 - 591.06, 659.74 - 639.95, 711.9 - 689.4])
max_intensity = np.array([7922.57, 13158.20, 17596.56, 20678.34, 21064.79, 15735.36, 14109.69, 8799.51])
comb_array =  np.transpose(np.array([width_est, max_intensity]))
spec_df = pd.DataFrame(data= comb_array, index= wavelengths, columns = ['Width Estimate', 'Max Intensity'])
