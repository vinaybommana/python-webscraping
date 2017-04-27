import os
import urllib.request
from bs4 import BeautifulSoup
import requests
#url = 'http://www.anits.edu.in/attendance.php?regdnor=on&regdno=' + str(i) + '&submit=Search..&mobile='
page1 = urllib.request.urlopen('http://www.anits.edu.in/attendance.php?regdnor=on&regdno=314126514016&submit=Search..&mobile='  )

soup = BeautifulSoup(page1, 'html.parser')

print(soup.get_text())

