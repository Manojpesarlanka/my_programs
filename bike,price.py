import requests
from bs4 import BeautifulSoup
import csv

url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

#links
links=[]
link=soup.findAll('div',class_="bikeDescWrapper")
for i in link:
    j=i.a['href']
    links.append(j)

bikeslist=[]
for i in links:
    bike=soup.find('h3',class_="bikeTitle margin-bottom10").text.strip()
    price =soup.find('span',class_="font18").text.strip()
    bikes={
        bike : price,   
    }
    bikeslist.append(bikes)
print(bikeslist)
