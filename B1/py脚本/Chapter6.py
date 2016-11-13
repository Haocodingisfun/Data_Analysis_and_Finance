import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.random.standard_normal((9, 4))
a.round(7)

a.round(6)

df = pd.DataFrame(a)
df

df.columns = [['No1', 'No2', 'No3', 'No4']]
df

#df['No2'][3]
#df

dates = pd.date_range('2005-1-1', periods=9, freq='M')
#dates

df.index = dates
df

np.array(df).round(6)

df.sum()

df.mean()

df.cumsum()

df.describe()

np.sqrt(df).sum()

%matplotlib 
df.cumsum().plot(lw=2.0)

type(df)

df['No1']

type(df['No1'])

df['No1'].cumsum().plot(style='r', lw=2.)
plt.xlabel('date')
plt.ylabel('value')

df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
df

groups = df.groupby('Quarter')

groups.mean()

groups.max()

groups.size()

df['Odd_even'] = ['Odd', 'Even', 'Odd', 'Even','Odd', 'Even','Odd', 'Even', 'Odd']

goups = df.groupby(['Quarter', 'Odd_even'])

groups.size()

groups.mean()

import pandas.io.data as web

DAX = web.DataReader(name='^GDAXI', data_source='yahoo', start='2000-1-1')
DAX.info()

DAX.tail()

DAX['Close'].plot(figsize=(8, 5))

import numpy as np
%%time
DAX['Ret_loop'] = 0.0
for i in range(1, len(DAX)):
	DAX['Ret_loop'][i] = np.log(DAX['Close'][i] / DAX['Close'][i - 1])

DAX[['Close', 'Ret_loop']].tail()

%time DAX['Return'] = np.log(DAX['Close'] / DAX['Close'].shift(1))
DAX[['Close', 'Ret_loop', 'Return']].tail()

del DAX['Ret_loop']

DAX[['Close', 'Return']].plot(subplots=True, style='b', figsize=(8, 5))

import pandas as pd
DAX['42d'] = pd.rolling_mean(DAX['Close'], window=43)
DAX['252d'] = pd.rolling_mean(DAX['Close'], window=252)

DAX[['Close', '42d', '252d']].tail()

DAX[['Close', '42d', '252d']].plot(figsize=(8, 5))

import math
DAX['Mov_Vol'] = pd.rolling_std(DAX['Return'], window=252) * math.sqrt(252)

DAX[['Close', 'Mov_Vol', 'Return']].plot(subplots=True, style='b', figsize=(8, 7))

import pandas as pd
from urllib import urlretrieve

es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
urlretrieve(es_url, './data/es.txt')
urlretrieve(vs_url, './data/vs.txt')
!ls -o ./data/*.txt	# 创建新文件夹

lines = open('./data/es.txt', 'r').readlines()
lines = [line.replace(' ', '') for line in lines]

lines[: 6]

for line in lines[3883:3890]:
	print line[41:],

new_file = open('./data/es50.txt', 'w')
new_file.writelines('data' + lines[3][:-1] + ';DEL' + lines[3][-1])
new_file.writelines(lines[4:])
new_file.close()

new_file = open('./data/es50.txt', 'r').readlines()
new_file[: 5]

es = pd.read_csv('./data/es50.txt', index_col=0, parse_dates=True, sep=';', dayfirst=True)
np.round(es.tail())

del es['DEL']
es.info()

cols = ['SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF', 'SXXA', 'DK5F', 'DKXF']
es = pd.read_csv(es_url, index_col=0, parse_dates=True, sep=';', dayfirst=True, header=None, skiprows=4, names=cols)
es.tail()

vs = pd.read_csv('./data/vs.txt', index_col=0, header=2, parse_dates=True, sep=',', dayfirst=True)
vs.info()

import datetime as dt
data = pd.DataFrame({'EUROSTOXX': es['SX5E'][es.index > dt.datetime(1999, 1, 1)]})
data = data.join(pd.DataFrame({'VSTOXX': vs['V2TX'][vs.index > dt.datetime(1999, 1, 1)]}))

data = data.fillna(method='ffill')
data.info()

data.tail()

data.plot(subplots=True, grid=True, style='b', figsize=(8,6))

rets = np.log(data / data.shift(1))
rets.head()

rets.plot(subplots=True, grid=True, style='b', figsize=(8, 6))
'''
xdat = rets['EUROSTOXX']
ydat = rets['VSTOXX']
model = pd.ols(y=ydat, x=xdat)
model
'''
rets1 = rets[1: 4034]
xdat1 = rets1['EUROSTOXX']
ydat1 = rets1['VSTOXX']
model1 = pd.ols(y=ydat1, x=xdat1)
model1

plt.plot(xdat1, ydat1, 'r.')
ax = plt.axis()
x = np.linspace(ax[0], ax[1] + 0.01)
plt.plot(x, model1.beta[1] + model1.beta[0] * x, 'b', lw=2)
plt.grid(True)
plt.axis('tight')
plt.xlabel('EURO STOXX 50 returns')
plt.ylabel('VSTOXX returns')

rets1.corr()

pd.rolling_corr(rets1['EUROSTOXX'], rets1['VSTOXX'], window=252).plot(grid=True, style='b')

import numpy as np
import pandas as pd
import datetime as dt
from urllib import urlretrieve
#%matplotlib 
'''
url1 = 'http://hopey.netfonds.no/posdump.php?'
url2 = 'date=%s%s%s&paper=AAPL.O&csv_format=csv'
url = url1 + url2
'''

#url = 'https://www.quandl.com/api/v3/databases/ASN100/download?api_key=<jYYuEzn4jsFadYZfZ9tz>&download_type=20160104'
year = '2016'
month = '10'
days = ['25', '26', '27', '28']
# dates might need to be updated
url = 'https://www.quandl.com/api/v3/databases/AS500/download?download_type=20151117-master&api_key=RcqEv1MVARkypbfGeb4d'

AAPL = pd.DataFrame()
for day in days:
	AAPL = AAPL.append(pd.read_csv(url % (year, month, day), index_col=0, header=0, parse_dates=True))
AAPL.columns = ['bid', 'bdepth', 'bdeptht', 'offer', 'odepth', 'odeptht']
# shorter colummn names



