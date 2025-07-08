#scrape cad.timken.com for housed units

import requests
from bs4 import BeautifulSoup

url = 'https://cad.timken.com/viewitems/split-cylindrical-roller-bearing-flange-units/split-cylindrical-roller-bearing-light-series-flan'
#url = 'https://cad.timken.com/viewitems/single-concentric-solid-block-mounted-bearings/single-concentric-two-bolt-pillow-block'
#url = 'https://cad.timken.com/viewitems/fafnir--pillow-block-mounted-bearings/fafnir--pillow-block-mounted-bearings-eccentric-lo'

r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

item_table = soup.find('table', id='plp-table-filter')  #this locates the table
#print(item_table)   #works
# i want both the header and data
# i also want to go to each page

for h in item_table.find_all('thead'):
    links = h.find_all('a')
    for link in links:   
        print(link.text.strip() )   #this returns a list of headers

#now need to return the body data.
#part will be a link all other data will simply be data

#need to find itemprop = 'sku' for part and itemprop = 'value' for data
for b in item_table.find_all('tbody'):
    #print (b.text.strip())
    for row in b.find_all('tr'):
        part = row.find('span', itemprop = 'sku')   #returns the part number but no link data
        data = row.find_all('span', itemprop = 'value')   # returns all data about the item
        print (part.text.strip())
        for d in data:
            print (d.text.strip())
        print('')      


        # SI and Imperial data is separated and needs to be combined somehow.
        # not sure if each housed unit type will present data teh same way.
  