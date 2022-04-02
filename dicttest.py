#!/usr/bin/python
from ast import Num
from asyncore import loop
from operator import contains
# from lib2to3.pytree import _Results
from re import X
import sys, csv
from csv import reader
import pandas as pd
from tkinter import N
from unicodedata import name
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
# line_count = 0
#read csv, and split on "," the line
file = open("attendance_test.csv", newline='')
csvreader = csv.reader(file, delimiter=',')
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
line_count = (len(rows))
#  file_name = 'attendance_test.csv'
# def count_lines_readlines(file_name):
#     fp = open(file_name,'r')
#     line_count = len(fp.readlines())
#     return line_count
#     return line_count
# print (line_count)
# print(results)

# with open('attendance_test.csv', newline='') as csvfile:
#     read_csv = csv.reader(csvfile, delimiter=",")
#     value = len(list(read_csv))
#     print (value)
#create two new lists: seniors and non-seniors
#first, initialize the lists
file = open("attendance_test.csv")
csvreader = csv.reader(file)
header = next(csvreader)
while line_count >= 1:
    for row in rows:
        if word_search in row[1]:
            print("Found! This one is a senior: ", row)
            seniors.append(row)
            line_count -= line_count 
        else:
            print("Not found! This one is NOT a senior: ", row)
            everyone_else.append(row)
            line_count -= line_count 

# everyone_else.remove(everyone_else[0])
print ("seniors list: ", seniors)
print ("non-seniors list: ", everyone_else)

#set the variables list item 0=name, 1=email address 2=atnum, 
# 3=skipnum, 4=attrate, 5=remaining_number of sessions, 6=still need to attend 
attrate = 0
remaining_number_sessions_seniors = 0
neednum_seniors = 0
neednum_everyone_else = 0
remaining_dates_seniors = [
4/4, 4/5, 4/6, 4/7, 
4/11, 4/12, 4/13, 4/14, 
4/18, 4/19, 4/20, 4/21, 
4/25, 4/26, 4/27, 4/28,
5/2, 5/3, 5/4, 5/5,
5/9, 5/10, 5/11, 5/12
] 
remaining_number_sessions_seniors = len(remaining_dates_seniors)
print ("number of sessions left for seniors: ", len(remaining_dates_seniors))

remaining_number_sessions_non_seniors = 0
remaining_dates_everyone_else = [
4/4, 4/5, 4/6, 4/7, 
4/11, 4/12, 4/13, 4/14, 
4/18, 4/19, 4/20, 4/21, 
4/25, 4/26, 4/27, 4/28,
5/2, 5/3, 5/4, 5/5,
5/9, 5/10, 5/11, 5/12,
5/16, 5/17, 5/18, 5/19,
] 
remaining_number_sessions_non_seniors = len(remaining_dates_everyone_else)
print ("number of sessions left for non-seniors: ", remaining_number_sessions_non_seniors)

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
            entry = "You must attend at least " + str(neednum_everyone_else) + " sessions in order to reach the critical threshold of the majority of practices (i.e. an attendance rate of more than 50%) and pass Spring Fitness." + '\n'
            email_report += entry
            email_report += str(inner_list) + '\n\n'
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
            entry = "You must attend at least " + str(neednum_seniors) + " sessions in order to reach the critical threshold of the majority of practices (i.e. an attendance rate of more than 50%) and pass Spring Fitness." + '\n'
            email_report += entry
            email_report += str(inner_list) + '\n\n'
            break             

#create a txt report that includes all students with the email message to be sent
with open('report.txt', 'w') as file:    
    file.write(email_report)

#email each student with customized email message

#create an end of year report with attendance records and a list of passing students

