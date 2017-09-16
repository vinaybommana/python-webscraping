import csv
# import requests
import urllib.request
from bs4 import BeautifulSoup

# csv is an acronym for comma seperated value
csv_file = csv.writer(open("EEE.csv", "w"))
# naming the first row of the file EEE-A.csv with columns regd.no, Name, Attendance_Percentage
csv_file.writerow(["regd.no", "Name","Total Classes Conducted","Total Classes Attended","Attendance_Percentage"])

# looping through the entire 65 members in the class
# you should give your desired roll number.
for i in range(1, 99):
    # opening the html files using urllib
    # python2 
    # urllib2.urlopen()
    page1 = urllib.request.urlopen('file:///home/vinay/me/mycodes/python/webscraping/EEE/file' + str(i) + '.html')
    # extracting the tags using BeautifulSoup library
    soup = BeautifulSoup(page1, 'html.parser')
    #print(soup.prettify())
    #tables = soup.findAll("table")
    #rows = soup.findAll("tr")
    #for row in rows:
    #    print(row.get_text())
    name = 5
    roll_no = 1
    Total_classes_conducted = 12
    Total_classes_attended = 13
    attendance_percentage = 14
    # row data is the list of all the cells in the student table
    row_data = soup.findAll("td")
    #print(row_data)
    # initializing the student name, rollno and Attendance_Percentage
    student_name = ''
    student_rollno = ''
    student_attendance_percentage = ''
    student_total_classes_attended = ''
    student_total_classes_conducted = ''
    for i in row_data:
        if row_data.index(i) == name:
            student_name = i.get_text()
        if row_data.index(i) == roll_no:
            student_rollno = i.get_text()
        if row_data.index(i) == attendance_percentage:
            student_attendance_percentage = i.get_text()
        if row_data.index(i) == Total_classes_conducted:
            student_total_classes_conducted = i.get_text()
        if row_data.index(i) == Total_classes_attended:
            student_total_classes_attended = i.get_text()
    csv_file.writerow([student_rollno, student_name,student_total_classes_conducted, student_total_classes_attended, student_attendance_percentage])
