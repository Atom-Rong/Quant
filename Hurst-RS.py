# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:51:43 2017
@author: atom
"""
import pandas as pd
import numpy as np
data=pd.read_excel(r'D:\atom\hurst\hurst.exe\data\shangzheng.xlsx')
data=np.array(data)
time_length=len(data[:,0])+1
date_list = pd.date_range(data[0,0], periods=time_length, freq='D')
ranges = ['1','2','4','8','16','32']
gap=[0 for i in range(len(ranges))]
sumnumber=0
for j  in range(len(ranges)):
    j=int(j)
    sumnumber=int(ranges[j])+sumnumber
ARS=[]
for i in range(len(ranges)):
    if i==0:
        gap[0] = time_length
    else:
        gap[i] = gap[0]/(2**i)
for r in range(len(ranges)):
    RS=list()
        #第i个片段
    for i in range(int(ranges[r])):
        Range = data[int(i*gap[r]):int((i+1)*gap[r]),1:2]
        meanvalue = np.mean(Range)     
        Deviation = Range - meanvalue
        maxi = max(Deviation)
        mini = min(Deviation)
        sigma = np.std(Range)
        RS=maxi-mini      
    ARS.append(np.mean(RS))
gap = np.log10(gap)
ARS = np.log10(ARS)
hurst_exponent = np.polyfit(gap,ARS,1)
hurst = hurst_exponent[0]*2
print(hurst)