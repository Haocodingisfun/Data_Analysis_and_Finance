path = '/Users/wonderful/data/'
import numpy as np
from random import gauss
a = [gauss(1.5, 2) for i in range(1000000)]
import pickle
pkl_file = open(path + 'data.pkl', 'w')
%time pickle.dump(a, pkl_file)
pkl_file
pkl_file.close()
#ll $path*
pkl_file = open(path + 'data.pkl', 'r') # open file for reading
%time b = pickle.load(pkl_file)
b[:5]
a[:5]
np.allclose(np.array(a), np.array(b))
np.sum(np.array(a) - np.array(b))
pkl_file = open(path + 'data.pkl', 'w') # open file for writing
%time pickle.dump(np.array(a), pkl_file)
%time pickle.dump(np.array(a) ** 2, pkl_file)
pkl_file.close()
#ll $path*
pkl_file = open(path + 'data.pkl', 'r')
x = pickle.load(pkl_file)
x
y = pickle.load(pkl_file)
y
pkl_file.close()
pkl_file = open(path + 'data.pkl', 'w')
pickle.dump({'x': x, 'y': y}, pkl_file)
pkl_file.close()
pkl_file = open(path + 'data.pkl', 'r') # open file for reading
data = pickle.load(pkl_file)
pkl_file.close()
for key in data.keys():
	print key, data[key][:4]
!rm -f $path*


rows = 5000
a = np.random.standard_normal((rows, 5))
a.round(4)
import pandas as pd
t = pd.date_range(start='2014/1/1', periods=rows, freq='H')
t
csv_file = open(path + 'data.csv', 'w')
header = 'date, no1, no2, no3, no4 no5\n'
csv_file.write(header)
for t_,(no1, no2, no3, no4, no5) in zip(t, a):
	s = '%s, %f, %f, %f, %f, %f\n' % (t_, no1, no2, no3, no4, no5)
	csv_file.write(s)
csv_file.close()
ll $path
csv_file = open(path + 'data.csv', 'r') # open file for reading
for i in range(5):
	print csv_file.readline(),
csv_file = open(path + 'data.csv', 'r')
content = csv_file.readlines()
for line in content[: 5]:
	print line
csv_file.close()
!rm -f $path*


import sqlite3 as sq3
query = 'CREATE TABLE numbs (Date data, No1 real, No2 real)'
con = sq3.connect(path + 'numbs.db')
con.execute(query)
con.commit()
import datetime as dt
con.execute('INSERT INTO numbs VALUES(?, ?, ?)', (dt.datetime.now(), 0.12, 7.3))
data = np.random.standard_normal((10000, 2)).round(5)
for row in data:
	con.execute('INSERT INTO numbs VALUES(?, ?, ?)', (dt.datetime.now(), row[0], row[1]))
con.commit()
con.execute('SELECT * FROM numbs').fetchmany(10)
pointer = con.execute('SELECT * FROM numbs')
for i in range(3):
	print pointer.fetchone()
csv_file.close()
!rm -f $path*
csv_file.close()
!rm -f $path*


import numpy as np
dtimes = np.arange('2015-01-01 10:00:00', '2021-12-31 22:00:00', dtype='datetime64[m]')
len(dtimes)
import numpy as np
dtimes = np.arange('2015-01-01 10:00:00', '2021-12-31 22:00:00', dtype='datetime64[m]')
len(dtimes)
dty = np.dtype([('Date', 'datetime64[m]'), ('No1', 'f'), ('No2', 'f')])
data = np.zeros(len(dtimes), dtype=dty)
data['Date'] = dtimes
a = np.random.standard_normal((len(dtimes), 2)).round(5)
data['No1'] = a[:, 0]
data['No2'] = a[:, 1]
%time np.save(path + 'array', data)
ll $path*
%time np.load(path + 'array.npy')
data = np.random.standard_normal((10000, 6000))
%time np.save(path + 'array', data)
ll $path*
data = 0.0
!rm -f $path*


import numpy as np
import pandas as pd
data = np.random.standard_normal((1000000, 5)).round(5)
filename = path + 'numbs'
import sqlite3 as sq3
query = 'CREATE TABLE numbers (No1 real, No2 real, No3 real, No4 real, No5 real)'
con = sq3.connect(filename + '.db')
con.execute(query)
#%%time
con.executemany('INSERT INTO numbers VALUES (?, ?, ?, ?, ?)', data)
con.commit()
#ll $path*
#%%time 
temp = con.execute('SELECT * FROM numbers').fetchall()
print temp[:2]
temp = 0.0
#%%time
query = 'SELECT * FROM numbers WHERE No1 > 0 AND No2 < 0'
res = np.array(con.execute(query).fetchall()).round(3)
res = res[:: 100]
import matplotlib.pyplot as plt
#%matplotlib inline
plt.plot(res[:, 0], res[:, 1], 'ro')
plt.grid(True)
plt.xlim(-0.5, 4.5)
plt.ylim(-4.5, 0.5)
plt.show()


import pandas.io.sql as pds 
%time data = pds.read_sql('SELECT * FROM numbers', con)
data.head()
%time data[(data['No1'] > 0) & (data['No2'] < 0)].head()
%time	# %%time 用不起来 
res = data[['No1', 'No2']][((data['No1'] > 0.5) | (data['No1'] < -0.5)) & ((data['No2'] < -1) | (data['No2'] > 1))]
plt.plot(res.No1, res.No2, 'ro')
plt.grid(True)
plt.axis('tight')


h5s = pd.HDFStore(filename + '.h5s', 'w')
%time temp = h5s['data']
h5s
h5s.close()
np.allclose(np.array(temp), np.array(data))
temp = 0.0


%time data.to_csv(filename + '.csv')
%time	# %%time 
pd.read_csv(filename + '.csv')[['No1', 'No2', 'No3', 'No4']].hist(bins=20)


%time data[: 100000].to_excel(filename + '.xlsx')
%time pd.read_excel(filename + '.xlsx', 'Sheet1').cumsum().plot()
ll $path*
!rm -f $path*


import numpy as np
import tables as tb 
import datetime as dt 
import matplotlib.pyplot as plt
%matplotlib inline
filename = path + 'tab.h5'
h5 = tb.open_file(filename, 'w')
rows = 2000000
row_des = {
	'Date': tb.StringCol(26, pos=1),
	'No1': tb.IntCol(pos=2),
	'No2': tb.IntCol(pos=3),
	'No3': tb.Float64Col(pos=4),
	'No4': tb.Float64Col(pos=5)
}
filters = tb.Filters(complevel=0)
tab = h5.create_table('/', 'ints_floats', row_des, title='Integers and Floats', expectedrows=rows, filters=filters)
tab
pointer = tab.row
ran_int = np.random.randint(0, 10000, size=(rows, 2))
ran_flo = np.random.standard_normal((rows, 2)).round(5)
%%time
for i in range(rows):
	pointer['Date'] = dt.datetime.now()
	pointer['No1'] = ran_int[i, 0]
	pointer['No2'] = ran_int[i, 1]
	pointer['No3'] = ran_flo[i, 0]
	pointer['No4'] = ran_flo[i, 1]
	pointer.append()
	# this appends the data and
	# moves the pointer one row forward
tab.flush()
tab 
#ll $path*
dty = np.dtype([('Date', 'S26'), ('No1', '<i4'), ('No2', '<i4'), ('No3', '<f8'), ('No4', '<f8')])
sarray = np.zeros(len(ran_int), dtype=dty)
sarray
%time	# %%time
sarray['Date'] = dt.datetime.now()
sarray['No1'] = ran_int[i, 0]
sarray['No2'] = ran_int[i, 1]
sarray['No3'] = ran_flo[i, 0]
sarray['No4'] = ran_flo[i, 1]
%time	# %%time
h5.create_table('/', 'ints_floats_from_array', sarray, title='Integers and Floats', expectedrows=rows, filters=filters)
h5
h5.remove_node('/', 'ints_floats_from_array')
tab[:3]
tab[:4]['No4']
%time np.sum(tab[:]['No3'])
%time np.sum(tab[:]['No1'])
%time np.sum(tab[:]['No3'])
%time	# %%time
plt.hist(tab[:]['No3'], bins=30)
plt.grid(True)
print len(tab[:]['No3'])
%time np.sum(tab[:]['No3'])
%time	# %%time
res = np.array([(row['No3'], row['No4']) for row in tab.where('((No3 < -0.5) | (No3 > 0.5)) & ((No4 < -1) | (No4 > 1))')])[::100]
plt.plot(res.T[0], res.T[1], 'ro')
plt.grid(True)
%time	# %%time
values = tab.cols
print 'Max %18.3d' % values.Max()
print 'Ave %18.3d' % values.Ave()
print 'Min %18.3d' % values.Min()
print 'Std %18.3d' % values.Std()
results = [(row['No1'], row['No2']) for row in tab.where('((No1 > 9800) | (No1 < 200)) & ((No2 > 4500) & (No2 < 5500))')]
for res in results[:4]:
	print res
results = [(row['No1'], row['No2']) for row in tab.where('(No1 == 1234) & (No2 > 9776)')]
for res in results:
	print res



filename = path + 'tab.h5c'
h5cfilename = path + 'tab.h5c'
h5c = tb.open_file(filename, 'w')
filters = tb.Filters(complevel=4, complib='blosc')
tabc = h5c.create_table('/', 'ints_floats', sarray, title='Integers and Floats', expectedrows=rows, filters=filters)
res = np.array([(row['No3'], row['No4']) for row in tabc.where('((No3 < -0.5) | (No3 > 0.5)) & ((No4 < -1) | (No4 > 1))')])[::100]= tb.open_file(filename, 'w')
%time arr_non = tab.read()
%time arr_non = tabc.read()
ll $path*
h5c.close()


#%%time
arr_int = h5.create_array('/', 'Integers', ran_int)
arr_flo = h5.create_array('/', 'floats', ran_flo)
h5
ll $path*



filename = path + 'array.h5'
h5 = tb.open_file(filename, 'w')
n = 1000
ear = h5.createEArray(h5.root, 'ear', atom=tb.Float64Atom(), shape=(0, n))
#%%time
rand = np.random.standard_normal((n, n))
for i in range(750):
	ear.append(rand)
ear.flush()
ear
ear.size_on_disk
out = h5.createEArray(h5.root, 'out', atom=tb.Float64Atom(), shape=(0, n))


expr = tb.Expr('3 * sin(ear) + sqrt(abs(ear))')
expr.setOutput(out, append_mode=True)
%time expr.eval()
out[0, :10]
%time imattar = ear.read()
import numexpr as ne
expr = '3 * sin(imarray) + sqrt(abs(imarray))'
ne.set_num_threads(16)
%time ne.evaluate(expr)[0, :10]