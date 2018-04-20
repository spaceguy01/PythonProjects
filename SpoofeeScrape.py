from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

# Website Spoofee.com that provides deals
html_url = 'http://www.spoofee.com/'

uClient = uReq(html_url)

page_html = uClient.read()

uClient.close()

page_soup = bs(page_html, 'html.parser')

# Pulling the Title and the Dates from posting. Only scrapes the first page, showing the last 2-3 days.
titles = page_soup.findAll("td",{"class":"dealtitle"})
date = page_soup.findAll("td",{"class":"date"})

dated = []
for day in date:
    dated.append(day.text.replace(","," - "))


# Creating a "spoofeedeals.csv" file to write the Tile and Deal Title
filename = "spoofeedeals.csv"
f = open(filename,"w")

headers = "Date and Deals\n"
f.write(headers)

for day  in dated:

    f.write('\n'+day +'\n\n')
    for title in titles:
        f.write(title.text+'\n')

f.close()
