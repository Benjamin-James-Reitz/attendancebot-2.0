#!/usr/bin/python

import sys, csv
from csv import DictReader, DictWriter
from typing import List, Dict

#split the list into two lists: seniors, and everyone else
#seniors last day is thurs, may 5th. ()
#everyone else last day is wed, May 25th

#input number you want to search
number = str(22)

#read csv, and split on "," the line
file_handle = open('attendance_test.csv', "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table_everyone = []
table_nonseniors = []
table_seniors = []

#create a table of all attendance records
for row in csv_reader:
    str_row: Dict = {}
    for column in row:
        str_row[column] = (row[column])
        table_everyone.append(str_row)
    break

print("table everyone: ", table_everyone)

#loop through the csv list and split it into two new dictionaries: seniors and everyone else
for row in table_everyone:
    str_row: Dict = {}
    for column in row:
        str_row[column] = (row[column])
        if number in row["email"]:
            table_seniors.append(str_row)
        else:
            table_nonseniors.append(str_row)
        break
    #if current rows 2nd value is equal to number add row to senior rates, if not add row to else rates.
    #if number in row[1]:
    #    'senior_rates.csv'.append(row)
        # First, open the old CSV file in append mode, hence mentioned as 'a'
# Then, for the CSV file, create a file object
print("seniors", table_seniors)
print("non seniors", table_nonseniors)
        #dict_writer_senior
    # Pass the CSV  file object to the Dictwriter() function
    # Result - a DictWriter object
    #    dictwriter_object = DictWriter(object, fieldnames=headersCSV)
    # Pass the data in the dictionary as an argument into the writerow() function
    #    dictwriter_object.writerow(list_data)
    # Close the file object
    #file_handle.close
    #else:
    #    csv_writer_else
    # Pass the CSV  file object to the Dictwriter() function
    # Result - a DictWriter object
    #    dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
    # Pass the data in the dictionary as an argument into the writerow() function
    #    dictwriter_object.writerow(dict)
    # Close the file object
    #    file_handle.close
    #row += row
#print(row in senior_rates.csv)


#from pprint import pprint

#set the variables
attrate = 0
attnum = 0
skipnum = 0
remnum = 0
neednum = 0

#interpret the data and convert into an int total of days attended
#    row = wks.row_values(name)
#    print(row[0])
   # del row[:5]

#    for days in row:
#        if days=="P":
#            attnum = attnum+1 
#        elif days=="A":
#            skipnum = skipnum+1
#            days += days
#        else:
#            if (skipnum+attnum) == 0:
#                attnum = 1
#        attrate = attnum / (skipnum+attnum)*100

#    print("attnum: ", attnum)
#    print ("skipnum: ", skipnum)
#    print("attrate: ", attrate)

#iterate over dict of this row(name), add 1 to attnum for each "P" in the row
#update attnum
#move to the next name and repeat

#calc skipnum
#calc attrate

#wks.update_cell(2,3, attnum)
#reset the variable counts
#    skipnum = 0
#    attnum = 0
#loop 
#print(" \n")
#name += 1
#pprint(wks.get_all_records())
#updating/modifying a cell

#calculate the number of practices left in the year and then how many sessions 
# minimum the student must attend to pass

#email each student with customized email message


