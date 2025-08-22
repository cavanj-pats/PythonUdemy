#scrape https://www.fisherhonda.com/honda-maintenance-codes/ for HONDA SERVICE CODES and their INTEVALS


import requests
from bs4 import BeautifulSoup
import pandas as pd



##############################################################################################################################



url = 'http://www.fisherhonda.com/honda-maintenance-codes/'

#########################################################################################################################



# 



# below works, don't believe it is needed anymore
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0'
    }
r = requests.get(url, headers=headers)
#r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

#####  The below is an old technique that worked perfectly fine  ##########################
#get the number of pages we need to naviage to:  this will become an outer loop
#navigation_List.append(url)
pages = soup.find('div', class_="zm-container zm-text-grid zm-text-grid-2 zm-align-top")

for h in pages.find_all('h4'):
    for p in h.find_all('p'):
        print (p.text)
    



