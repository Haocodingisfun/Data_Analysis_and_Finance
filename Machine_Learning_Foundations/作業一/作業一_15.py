import pandas as pd
import numpy as np
import random

# 整理为 DataFrame 格式
data = np.fromfile('hw1_15_train.dat', sep=' ', dtype=float)
df = pd.DataFrame(index=range(int(len(data)/5)), columns=['x0', 'x1', 'x2', 'x3', 'x4', 'y'])
df['x0'] = 1.0
df['x1'] = data[::5]
df['x2'] = data[1::5]
df['x3'] = data[2::5]
df['x4'] = data[3::5]
df['y'] = data[4::5]

# time 为迭代次数
time = 0
# 初始权重
W = [.0, .0, .0, .0, .0]
while True:

    # 分别计算每一个数值和权重的乘积
    df['x0 * W'] = df['x0'] * W[0]
    df['x1 * W'] = df['x1'] * W[1]
    df['x2 * W'] = df['x2'] * W[2]
    df['x3 * W'] = df['x3'] * W[3]
    df['x4 * W'] = df['x4'] * W[4]
    
    # 汇总得分
    df['socre'] = df.iloc[:, 6:11].sum(axis=1)
    # 得分 => +1 或 -1
    df['sign'] = np.sign(df['socre'])
    df['sign'][:][df['sign'] == 0] = -1
    # 如于资料中的 y 不等，则 error 记为 1，否则为 0 
    df['error'] = 0
    df['error'][:][df['sign'] != df['y']] = 1
    # index 为错误的位置的集合
    index = df['error'][df['error'] == 1].index
    #if index.any():
    # 如果有错
    if len(index) != 0:
        # 在第一个犯错的地方改正
        num = index[0]
        W = W + df.iloc[num, 0:5] * df.iloc[num, 5] 
        # 迭代次数 +1
        time += 1
    else:
        print('迭代次数为: %s' % time)
        print('权重为: %s' % W)
        break
    