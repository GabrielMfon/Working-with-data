import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    #Printing the headers and their positions
    """for index, column_reader in enumerate(header_row):
        print(index, column_reader)"""

    #Get dates, high temperatures from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

print(highs)

#Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')


#format plot
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('',fontsize=16)

#prevent overlapping of the dates
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
