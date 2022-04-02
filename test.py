remaining_number_sessions_non_seniors = 28
neednum_everyone_else = 0
attnum = 4
skipnum = 4

neednum_everyone_else = remaining_number_sessions_non_seniors
while neednum_everyone_else >= 0:
    neednum_everyone_else = neednum_everyone_else - 1
    if (attnum+neednum_everyone_else)/(attnum+skipnum+remaining_number_sessions_non_seniors) <= 0.5:
        break
    print(neednum_everyone_else)
print("loop is finished")