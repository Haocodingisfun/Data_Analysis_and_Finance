import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)
y[:, 0] = y[:, 0] * 100
plt.figure(figsize=(7, 4))
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 1], lw=1.5, label='2nd')
plt.plot(y, 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show()


#------------------------------------------------

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)

fig, ax1 = plt.subplots()
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.legend(loc=8)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value 1st')
plt.title('A Simple Plot')
ax2 = ax1.twinx()
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.ylabel('value 2nd')
plt.show()

#------------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)

plt.figure(figsize=(9, 4))
plt.subplot(121)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('1st Data Set')

plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], color='g', width=0.5, label='2nd')
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.title('2nd Data Set')

plt.show()

#------------------------------------------------

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 5))
plt.plot(y[:, 0], y[:, 1],'ro')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')

plt.show()

#------------------------------------------------

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 5))
plt.scatter(y[:, 0], y[:, 1], marker='o')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')

plt.show()

#------------------------------------------------

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2))
c = np.random.randint(0, 10, len(y))
plt.figure(figsize=(7, 5))
plt.scatter(y[:, 0], y[:, 1], c=c, marker='o')
plt.colorbar()
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')

plt.show()


#------------------------------------------------

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 4))
plt.hist(y, label=['1st', '2nd'], bins=25)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')

plt.show()

#------------------------------------------------


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 4))
plt.hist(y, label=['1st', '2nd'], color=['b','g'], stacked=True, bins=25)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')

plt.show()

#------------------------------------------------


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2))
fig, ax = plt.subplots(figsize=(7, 4))
plt.boxplot(y)
plt.grid(True)
plt.setp(ax, xticklabels=['1st', '2nd'])
plt.xlabel('data set')
plt.ylabel('value')
plt.title('Bosplot')

plt.show()

#------------------------------------------------


import numpy as np
from matplotlib.patches import Polygon
def func(x):
	return 0.5 * np.exp(x) + 1
a, b =0.5, 1.5
x = np.linspace(0, 2)
y = func(x)
fig, ax = plt.subplots(figsize=(7, 5))
plt.plot(x, y, 'b', linewidth=2)
plt.ylim(ymin=0)
Ix = np.linspace(a, b)
Iy = func(Ix)
verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')
ax.add_patch(poly)
plt.text(0.5 * (a + b), 1, r"$\int_a^b f(x)\mathrm{d}x$",
		horizontalalignment='center', fontsize=20)
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([func(a), func(b)])
ax.set_yticklabels(('$f(a)$', '$f(b)$'))
plt.grid(True)
plt.show()

#------------------------------------------------


import matplotlib.finance as mpf
import matplotlib.pyplot as plt
start = (2014, 5, 1)
end = (2014, 6, 30)

quotes = mpf.quotes_historical_yahoo_ochl('^GDAXI', start, end)
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick_ochl(ax, quotes, width=0.6, colorup='b', colordown='r')
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.show()

#------------------------------------------------


import matplotlib.finance as mpf
import matplotlib.pyplot as plt
start = (2014, 5, 1)
end = (2014, 6, 30)

quotes = mpf.quotes_historical_yahoo_ochl('^GDAXI', start, end)
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)
mpf.plot_day_summary_oclh(ax, quotes, colorup='b', colordown='r')
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
plt.title('DAX Index')
plt.ylabel('index level')
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.show()



#------------------------------------------------



import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

strike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)

strike[: 2]

iv = (strike - 100) ** 2 / (100 * strike) /ttm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')

surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)

ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
#------------------------------------------------


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

strike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)

strike[: 2]

iv = (strike - 100) ** 2 / (100 * strike) /ttm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='^')

ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')

plt.show()