import matplotlib.finance as mpf
import matplotlib.pyplot as plt
start = (2014, 5, 1)
end = (2014, 6, 30)

quotes = mpf.quotes_historical_yahoo_ochl('^GDAXI', start, end)
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)
mpf.plot_day_summary_ochl(ax, quotes, colorup='b', colordown='r')
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
plt.title('DAX Index')
plt.ylabel('index level')
plt.setp(plt.gca().get_xticklabels(), rotation=30)