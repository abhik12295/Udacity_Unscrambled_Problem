"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

directory = dict()
for i in range(len(calls)):
    #calling telephone-->key and its corresponding time stamp-->value
    directory[calls[i][0]]= directory.get(calls[i][0],0) + int(calls[i][3])
    #receiving telephone-->key and its corresponding time stamp-->value
    directory[calls[i][1]]= directory.get(calls[i][1],0) + int(calls[i][3])

longest_time = 0
for time in directory.keys():
    if directory[time] > longest_time:
        longest_time = directory[time]

for number,time in directory.items():
    if time==longest_time:
        print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number,time)) 
