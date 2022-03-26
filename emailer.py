import yagmail

yag = yagmail.SMTP()
contents = [
    "Hello there from Mr. Reitz's Python3 Attendancebot. Your current attendance records are in the attached pdf. Please email breitz@saes.org if you have any questions."
]
yag.send('to@someone.com', 'subject', contents)
filename = "studentname-attendance.pdf"
# Alternatively, with a simple one-liner:
#yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', contents)
