from typing import ForwardRef
import requests
from bs4 import BeautifulSoup
import csv

url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

bikes={'bikenames':[]}
link=soup.findAll('div',class_="bikeDescWrapper")
for i in link:
    j=i.a.text
    bikes['bikenames'].append(j)
print(bikes)