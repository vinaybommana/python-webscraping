import requests
import urllib.request
from bs4 import BeautifulSoup
#url = 'http://www.anits.edu.in/attendance.php?regdnor=on&regdno=314126514016&submit=Search..&mobile='
#response = requests.get(url)
#html = response.content
#htmlfile = open("file2.html", "w+")
#htmlfile.write(html)
page1 = urllib.request.urlopen('file:///home/vinay/me/mycodes/python/webscraping/file' + '314126514001' + '.html')
soup = BeautifulSoup(page1, "lxml")
tables = soup.findAll("table")
print(tables)
rows = soup.findAll("tr")
for row in rows:
    print(row.get_text())

