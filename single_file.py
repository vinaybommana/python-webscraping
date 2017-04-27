import csv
import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('file:///home/vinay/me/mycodes/python/webscraping/EEE-A/file' + '314126514016' + '.html')

soup = BeautifulSoup(page, 'html.parser')
row_data = soup.findAll("td")
name = 5
roll_no = 1
percentage = 14
csv_file = csv.writer(open("example1.csv", "w"))
csv_file.writerow(["regd.no", "Name", "Attendance_Percentage"])
student_name = ''
student_rollno = ''
student_percentage = ''
for i in row_data:
    if row_data.index(i) == name:
        student_name = i.get_text()

    if row_data.index(i) == roll_no:
        student_rollno = i.get_text()

    if row_data.index(i) == percentage:
        student_percentage = i.get_text()
csv_file.writerow([student_rollno, student_name,student_percentage])

