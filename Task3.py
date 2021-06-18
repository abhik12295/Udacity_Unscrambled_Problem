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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#Part A
check_prefix = set()
callingBang = 0
calledBang= 0
#iterating over all 3 types of telephone number
for call in calls:
    if("(080)"==call[0][0:5]): #bangalore number
        callingBang = callingBang+1
        #area code begin with 0
        if("(0"==call[1][0:2]):
            check_paran= call[1].find(")")
            check_prefix.add(call[1][0:check_paran+1])
        #mobile without paranthesis and have space in middle + starts with either 7, 8 or 9
        elif(" " in call[1] and (call[1][0]=="7") or call[1][0]=="8" or call[1][0]=="9" ): 
            check_prefix.add(call[1][0:4])
        #Telemarketer number starts with 140 
        elif("140"==cals[1][0:3]):
            check_prefix.add(call[1][0:4])
        
        if("(080)"==call[1][0:5]): #add called number from bangalore to calledBang
            calledBang = calledBang+1
            
check_prefix = sorted(check_prefix)
print("The numbers called by people in Bangalore have codes: ")
for code in check_prefix:
    print("{}".format(code))
    
#Part B
percent_call = round((calledBang/callingBang)*100 , 2) #rounding number upto 2 decimal digits
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(percent_call))