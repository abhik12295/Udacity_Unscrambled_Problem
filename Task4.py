"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoing_call = set() 
receive_call = set()
send_text = set()
receive_text = set()

#selected outgoing and incoming calls
for call in calls:
    outgoing_call.add(call[0])
    receive_call.add(call[1])
#selected outgoing and incoming texts
for text in texts:
    send_text.add(text[0])
    receive_text.add(text[1])

#listed out by eliminating received call, sent text and received text
tele_market = list(outgoing_call - receive_call - send_text - receive_text) 
print("These numbers could be telemarketers: ")
for tele in sorted(tele_market):
    print(tele)
