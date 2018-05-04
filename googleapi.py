import urllib.parse
import requests

"""Input short address to get Full Address using GoogleAPI"""

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:

    address = input('\nInput Address or quit/q to Quit: ')

    if address.lower() == 'quit' or address.lower() =='q':

        break

    url = main_api + urllib.parse.urlencode({'address':address})

    json_data = requests.get(url).json()

    print ('URL: '+ url)


    json_status = json_data['status']

    print ('API Status: ' + json_status + '\n')

    if json_status == 'OK':

        for each in json_data['results'][0]['address_components']:

            print (each['long_name'])

        print ('-------------RESULT--------------')

        formatted_address = json_data['results'][0]['formatted_address']
