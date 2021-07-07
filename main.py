import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# get data
file_data = pd.read_csv('vax_malaysia.csv')
vax_date = file_data['date'].tolist()
vax_daily = file_data['total_daily'].tolist()

# initialisation
## insert rolling days here
win_1 = 7
win_2 = 14
win_3 = 30
new = np.arange(len(vax_date)) #date indexing

# functions
## get rolling average
def get_rolling(window_size):
    num_series = pd.Series(vax_daily)
    rolling_mean = num_series.rolling(window_size).mean().tolist()
    rolling_list = rolling_mean[window_size-1:]

    return rolling_list

# bar graph
plt.bar(vax_date, vax_daily)
plt.xticks(rotation=270)

# rolling average
## rolling 7
plt.plot(new[(win_1-1):], get_rolling(win_1), color='y', linestyle='dashed', label= str(win_1) + ' Days')
# rolling 14
plt.plot(new[(win_2-1):], get_rolling(win_2), color='r', linestyle='dashed', label= str(win_2) + ' Days')
# rolling 30
plt.plot(new[(win_3-1):], get_rolling(win_3), color='m', linestyle='dashed', label= str(win_3) + ' Days')

plt.title('Malaysia Daily Vaccine Doses\nAs of 6 July 2021')
plt.xlabel('Date')
plt.ylabel('Number of Doses Administer')
plt.legend(loc='upper left')
plt.show()
