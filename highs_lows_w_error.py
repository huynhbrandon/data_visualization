import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'death_valley_2014.csv'


#Get dates, high, and low temperatures from file.
with open(filename, newline ='') as f:	#open file name as f 
    reader = csv.reader(f)	# pass reader function file name and make it a reader object
    header_row = next(reader)	# next() returns the next line in the file passed

    dates, highs, lows = [], [], []
    for row in reader:
        #print(row[0])
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
   # print (highs)

#reader stores each line as list


#Plot Data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1) #fills between two lines

#format plot
title = "Daily high and low temperatures - 2004 \n Death Valley, CA"
plt.title(title, fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize= 10)

plt.show()




#for index, column_header in enumerate(header_row): #enumerate gets index of each item, and value
 #   print(index, column_header)

