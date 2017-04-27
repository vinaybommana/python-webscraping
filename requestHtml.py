### python libraries
import os
import requests
##############

## downloading html data using requests library
# changing the directory from webscraping to EEE-A
os.chdir('/home/vinay/me/mycodes/python/webscraping/EEE')

# looping through the entire 65 members
for i in range(314126514001, 314126514066):
    url = 'http://www.anits.edu.in/attendance.php?regdnor=on&regdno='+str(i)+'&submit=Search..&mobile='
    response = requests.get(url)
    html = response.content
    # storing the url content in '.html' format
    htmlfile = open("file" + str(i) + ".html", "wb")
    # writing the html file
    htmlfile.write(html)
