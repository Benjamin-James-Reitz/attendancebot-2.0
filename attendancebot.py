#setup the program modules from turtle import update
from unittest import skip
import gspread
from pprint import pprint
sa = gspread.service_account()
sh = sa.open("Spring Fitness Attendance 2022")
wks = sh.worksheet("Recipients")

#set the variables
attrate = 0
days = 0
attnum = 0
skipnum = 0
name = 2

#set up the command line argument inputs
import sys
print ("Number of arguments: ", len(sys.argv), "arguments.")
print ("Argument List: ", str(sys.argv))

#link the command line arguments to the name variable
print (sys.argv[1])
name = int(sys.argv[1])

#change the argv to a range between x, arg[1]
for name in range(19, name+1):    

#working with the sheet
    #print ('Rows: ', wks.row_count)
    #print ('Columns: ', wks.col_count)
    #print (wks.acell('A9').value)
    #print (wks.get('A1:B7'))


    #truncate data field to start on day 1, calculate attnum
#row = wks.row_values(name)
#print(row[0])
#del row[:5]

#interpret the data and convert into an int total of days attended
    row = wks.row_values(name)
    print(row[0])
    del row[:5]

    for days in row:
        if days=="P":
            attnum = attnum+1 
        elif days=="A":
            skipnum = skipnum+1
            days += days
        else:
            if (skipnum+attnum) == 0:
                attnum = 1
        attrate = attnum / (skipnum+attnum)*100

    print("attnum: ", attnum)
    print ("skipnum: ", skipnum)
    print("attrate: ", attrate)

#iterate over dict of this row(name), add 1 to attnum for each "P" in the row
#update attnum
#move to the next name and repeat

#calc skipnum
#calc attrate

#wks.update_cell(2,3, attnum)

    cell = wks.cell(name,3).value
    wks.update_cell(name,3, attrate)
    cell = wks.cell(name,4).value
    wks.update_cell(name,4, attnum)
    cell = wks.cell(name,5).value
    wks.update_cell(name,5, skipnum)
#reset the variable counts
    skipnum = 0
    attnum = 0
#loop 
print(" \n")
name += 1
#pprint(wks.get_all_records())
#updating/modifying a cell

#generate pdfs - link to google sheets script - how can I reference python variables?

#email each student with pdf attachment and email message




