#!/usr/bin/python
# from ast import Num
# from asyncore import loop
# from operator import contains
# from lib2to3.pytree import _Results
from re import X
import sys, csv
from csv import reader
# import pandas as pd
# from tkinter import N
# from unicodedata import name
#from optparse import Values
#from unicodedata import name

#create a report.txt file and email_report str
file = open('report.txt', 'w')
email_report = ""

#search string for "22" to sort out the seniors (the year 
# they will graduate is built into their email addresses)
word_search = str(22)
seniors = []
everyone_else = []

#read csv, and split on "," the line
file = open("attendance_test.csv", newline='')
csvreader = csv.reader(file, delimiter=',')
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
line_count = (len(rows))

#create two new lists: seniors and non-seniors
#first, initialize the lists
file = open("attendance_test.csv")
csvreader = csv.reader(file)
header = next(csvreader)
while line_count >= 1:
    for row in rows:
        if word_search in row[1]:
            # print("Found! This one is a senior: ", row)
            seniors.append(row)
            line_count -= line_count 
        else:
            # print("Not found! This one is NOT a senior: ", row)
            everyone_else.append(row)
            line_count -= line_count 

# everyone_else.remove(everyone_else[0])
# print ("seniors list: ", seniors)
# print ("non-seniors list: ", everyone_else)

#set the variables list item 0=name, 1=email address 2=atnum, 
# 3=skipnum, 4=attrate, 5=remaining_number of sessions, 6=still need to attend 7=email message
attrate = 0
remaining_number_sessions_seniors = 0
neednum_seniors = 0
neednum_everyone_else = 0
remaining_dates_seniors = [
'4-4', '4-5', '4-6', '4-7', 
'4-11', '4-12', '4-13', '4-14', 
'4-18', '4-19', '4-20', '4-21', 
'4-25', '4-26', '4-27', '4-28',
'5-2', '5-3', '5-4', '5-5'
] 
print(remaining_dates_seniors)
remaining_number_sessions_seniors = len(remaining_dates_seniors)
remaining_dates_sessions_seniors_string=''
remaining_dates_sessions_seniors_string=''.join([str(item) + ", " for item in remaining_dates_seniors])
# print ("number of sessions left for seniors: ", len(remaining_dates_seniors))
remaining_dates_sessions_seniors_string_stripped=remaining_dates_sessions_seniors_string[:-2]
print(remaining_dates_sessions_seniors_string)

remaining_number_sessions_non_seniors = 0
remaining_dates_everyone_else = [
'4-4', '4-5', '4-6', '4-7', 
'4-11', '4-12', '4-13', '4-14', 
'4-18', '4-19', '4-20', '4-21', 
'4-25', '4-26', '4-27', '4-28',
'5-2', '5-3', '5-4', '5-5',
'5-9', '5-10', '5-11', '5-12',
'5-16', '5-17', '5-18', '5-19'
] 
print(remaining_dates_everyone_else)

remaining_number_sessions_non_seniors = len(remaining_dates_everyone_else)
# print ("number of sessions left for non-seniors: ", remaining_number_sessions_non_seniors)
remaining_dates_everyone_else_string=''
remaining_dates_everyone_else_string=''.join([str(item) + ", " for item in remaining_dates_everyone_else])

remaining_dates_everyone_else_string_stripped=remaining_dates_everyone_else_string[:-2]
print (remaining_dates_everyone_else_string_stripped)

# Step 1: process attendance data for non-seniors and insert attnum, skipnum, attrate,  
# remaining_number_sessions_non_seniors, and neednum_everyone_else into list

for inner_list in everyone_else:
    skipnum = 0
    attnum = 0
    for i in inner_list:
        print([[i]])
        if i=="P":
            attnum = attnum+1 
        elif i=="A":
            skipnum = skipnum+1
            i += i
        # if (int(skipnum)+int(attnum)) == 0:
        #     attnum = 1
    print("attnum: ", attnum)
    print(type(attnum))
    inner_list.insert(2, attnum)
    print ("skipnum: ", skipnum)
    inner_list.insert(3, skipnum)
    print(type(skipnum))
    print ("attnum + skipnum: ", attnum + skipnum)
    attrate = ((attnum/(attnum+skipnum))*100)
    inner_list.insert(4, attrate)
    print("attrate: ", attrate, "%")
    print("# of remaining practices for non-seniors", remaining_number_sessions_non_seniors)
    inner_list.insert(5, remaining_number_sessions_non_seniors)

# calculate the minimum needed sessions to pass with more than 50% attendance
    neednum_everyone_else = remaining_number_sessions_non_seniors
    while neednum_everyone_else >= 0:
        neednum_everyone_else = neednum_everyone_else - 1
        if (attnum+neednum_everyone_else)/(attnum+skipnum+remaining_number_sessions_non_seniors) <= 0.5:
            neednum_everyone_else = neednum_everyone_else + 1
            inner_list.insert(6, neednum_everyone_else)
# write the student data to txt report file
            entry = "Dear " + inner_list[0] + ",\n\n    Greetings from Mr. Reitz' Python3 attendancebot. You still need to attend at least " + str(inner_list[6]) + " practices of the remaining " + str(inner_list[5]) + " in the school year in order to reach the critical threshold of the majority of practices (i.e. an attendance rate of more than 50%) and pass Spring Fitness. Your remaining practice dates are: " + remaining_dates_everyone_else_string_stripped + ".\n\nIn addition there will be two optional make-up practices on 5/23 and 5/24. \n\nIf you have any questions about this automated attendance notification, please reach out to my programmer, Mr Reitz, at breitz@saes.org \n\nSincerely, \nMr Reitz' Python3 Attendancebot \n\n"
            email_report += str(entry)
            inner_list.insert(7, email_report)
            email_report += "\n"
            break     
# Step 2: process attendance data for seniors and insert attnum, skipnum, attrate,  
# remaining_number_sessions_non_seniors, and neednum_everyone_else into list

for inner_list in seniors:
    skipnum = 0
    attnum = 0
    for i in inner_list:
        print([[i]])
        if i=="P":
            attnum = attnum+1 
        elif i=="A":
            skipnum = skipnum+1
            i += i
    print("attnum: ", attnum)
    print(type(attnum))
    inner_list.insert(2, attnum)
    print ("skipnum: ", skipnum)
    inner_list.insert(3, skipnum)
    print(type(skipnum))
    print ("attnum + skipnum: ", attnum + skipnum)
    attrate = ((attnum/(attnum+skipnum))*100)
    inner_list.insert(4, attrate)
    print("attrate: ", attrate, "%")
    print("# of remaining practices for seniors", remaining_number_sessions_seniors)
    inner_list.insert(5, remaining_number_sessions_seniors), 

# calculate the minimum needed sessions to pass with more than 50% attendance
    neednum_seniors = remaining_number_sessions_seniors
    while neednum_seniors >= 0:
        neednum_seniors = neednum_seniors - 1
        if (attnum+neednum_seniors)/(attnum+skipnum+remaining_number_sessions_seniors) <= 0.5:
            neednum_seniors = neednum_seniors + 1
            inner_list.insert(6, neednum_seniors) 
# write the student data to txt report file        
            entry = "Dear " + inner_list[0] + ",\n\n   Greetings from Mr. Reitz' Python3 attendancebot. You still need to attend at least " + str(inner_list[6]) + " practices of the remaining " + str(remaining_number_sessions_seniors) + " in the school year in order to reach the critical threshold of the majority of practices (i.e. an attendance rate of more than 50%) and pass Spring Fitness. Your remaining practice dates are: " + remaining_dates_sessions_seniors_string_stripped + ". \n\nIn addition there will be four optional/make-up practices on: 5-9, 5-10, 5-11, 5-12. \n\nIf you have any questions about this automated attendance notification, please reach out to my programmer, Mr Reitz, at breitz@saes.org \n\nSincerely, \nMr Reitz' Python3 Attendancebot \n\n"
            email_report += str(entry)
            inner_list.insert(7, email_report)
            email_report += "\n"
            break             

#create a txt report that includes all students with the email message to be sent
with open('report.txt', 'w') as file:    
    file.write(email_report)

#email each student with customized email message

#create an end of year report with attendance records and a list of passing students