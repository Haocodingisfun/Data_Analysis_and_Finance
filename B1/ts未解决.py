import matplotlib.finance as mpf
import matplotlib.pyplot as plt
import numpy as np
import tushare as ts

start = '2016-09-01'
end = '2016-09-30'
quotes = ts.get_hist_data('sh', start=start, end=end)

quotes = quotes[['open', 'close', 'high', 'low']]  # type(quotes) == pandas.core.frame.DataFrame
quotes1 = np.array(dadaquote)   # type(quotes1) == numpy.ndarray
quotes2 = pd.DataFrame(quotes1)  # type(quotes2) == pandas.core.frame.DataFrame
quotes3 = list(quotes1)  # type(quotes2) == list
date = quotes.index  # type(date) == numpy.ndarray
date1 = pd.DataFrame(date)  # type(date1) == pandas.core.frame.DataFrame
date2 = list(date)   # type(date2) == list
quote = quotes.join(pd.DataFrame(list(date), columns=['date',]) , how='outer')  # type(quote) == pandas.core.frame.DataFrame
quote1 = np.array(quote)  # type(quote1) == numpy.ndarray
quote2 = list((quote1)   # type(quote2) == list
'''
opens = quotes['open']
closes = quotes['close']
highs = quotes['high']n
lows = quotes['low']
'''

fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick_ochl(ax, list, width=0.6, colorup='b', colordown='r')
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.show()