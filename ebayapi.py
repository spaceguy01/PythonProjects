from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

Keywords = input("Enter your Keyword/s (ex: white piano):\n")
api = finding(appid='JoonYi-APIPytho-PRD-3e0516b4c-ff87a3f3', config_file=None)
api_request = {'keywords': Keywords, 'outputSelector': 'SellerInfo'}

response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

try:
    for each in items[0:15]:
        print('\n')
        print('Title is : ' +each.title.text)
        print('Payment method is : ' + each.paymentmethod.text)
        print('Item is located in : ' + each.location.text)
        print('This seller has a positive feedback rating of : ' + each.positivefeedbackpercent.text + ' out of 100')
        print('The current price of the item is : $' + each.currentprice.text)
        if each.conditiondisplayname:
            print('The item status is : ' + each.conditiondisplayname.text)
        else:
            print('There is no Current Status indicator for this item!')
        
except:
    pass
