from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


#URL
page = 'https://www.youtube.com/feed/trending'

# Open the url
uClient = uReq(page)

# Read the page
page_html = uClient.read()

#Close the url
uClient.close()

# soup the page
page_soup = bs(page_html, 'html.parser')

contents = page_soup.findAll("a",{"class":"yt-uix-tile-link"})

for each in contents:
    print (each.text)
