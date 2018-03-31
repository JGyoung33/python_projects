import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

filename = r'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #获取最高温及日期
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            high = int(row[1])

            date = datetime.strptime(row[0], '%Y-%m-%d')
            low = int(row[3])
        except ValueError:
            print(date,'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

    fig =plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)
    plt.title("daily high and low temperature in 2014",fontsize=24)
    plt.xlabel("",fontsize=16)
    plt.ylabel("value of temperature",fontsize=16)
    plt.ylim(20,120)
    fig.autofmt_xdate()
    plt.tick_params(axis='both',which = 'major',labelsize = 16)
    plt.show()

