#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:15:32 2016

@author: wonderful
"""

'''
一共四张图
但是只能输出三张
其中两张部分重叠
原因未知
尝试用subplot失败	
'''

import numpy as np
import tushare as ts
import matplotlib.pyplot as plt

sh = ts.get_hist_data('sh', start='2014-01-01', end='2016-04-14')
t1 = sh.info()
t2 = sh[['close', 'ma5', 'ma20']].tail()

sh['close'].plot(grid=True, figsize=(8, 5))
ax = plt.gca()
ax.invert_xaxis()

sh[['close', 'ma5', 'ma20']].plot(grid=True, figsize=(8, 5))
ax = plt.gca()
ax.invert_xaxis()

sh['ma5 - ma20'] = sh['ma5'] - sh['ma20']
t3 = sh['ma5 - ma20'].tail()
t4 = sh['ma5 - ma20'].head()

SD = 50
sh['Regime'] = np.where(sh['ma5 - ma20'] > SD, 1, 0)
sh['Regime'] = np.where(sh['ma5 - ma20'] < -SD, -1, sh['Regime'])
t5 = sh['Regime'].value_counts()

sh['Regime'].plot(lw=1.5)
plt.ylim(-1.1, 1.1)
ax = plt.gca()
ax.invert_xaxis()

sh['Market'] = np.log(sh['close'] / sh['close'].shift(1))
sh['Strategy'] = sh['Regime'].shift(1) * sh['Market']
sh[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True, figsize=(8, 5))
ax = plt.gca()
ax.invert_xaxis()

print t1, t2, t3, t4, t5
plt.show()
