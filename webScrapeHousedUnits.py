#scrape cad.timken.com for housed units

import requests
from bs4 import BeautifulSoup
import pandas as pd

#two Bolt Pillow /Plummer block
#four Bolt Pillow / Plummer Block
#four bolt flange
#two bolt flange
#Piloted flange
#cartridge

#various URL tests.  All seem to work.
#now need to figure out data structure, storage, and navigating to 
    # next pages
    # item detail data
data_listA=[]
colNames=[]
navigation_List=[]
url_pre = 'https://cad.timken.com'
#url = 'https://cad.timken.com/viewitems/split-cylindrical-roller-bearing-flange-units/split-cylindrical-roller-bearing-light-series-flan'
#url = 'https://cad.timken.com/viewitems/split-cylindrical-roller-bearing-light-series-plum/split-cylindrical-roller-bearing-light-series-stan'
#url = 'https://cad.timken.com/viewitems/single-concentric-solid-block-mounted-bearings/single-concentric-two-bolt-pillow-block'
#url = 'https://cad.timken.com/viewitems/fafnir--pillow-block-mounted-bearings/fafnir--pillow-block-mounted-bearings-eccentric-lo'
url = 'https://cad.timken.com/viewitems/split-cylindrical-roller-bearing-light-series-plum/split-cylindrical-roller-bearing-light-series-stan?pagesize=25&amp;sortid=140&amp;measuresortid=0&amp;pagenum=6'
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')


#get the number of pages we need to naviage to:  this will become an outer loop
navigation_List.append(url)
pages = soup.find('div', class_="plp-pagination")
for p in pages.find_all('a'):
    #print (url_pre + p.get('href'))
    navigation_List.append(url_pre + p.get('href'))



# must make list of links manually
#navigation_List.append(url)
#for x in range(20,22):  #there are 65 pages
#    navigation_List.append('https://cad.timken.com/viewitems/split-cylindrical-roller-bearing-light-series-plum/split-cylindrical-roller-bearing-light-series-stan?pagesize=25&amp;sortid=140&amp;measuresortid=0&amp;pagenum='+str(x))

firstFirstItem = True
#############################################  outer loop goes here 
##   1. For each set of tables within a product type,  top level page should be identical.  no need to check if columns exist.  Assumption
for pg in navigation_List:
    rr = requests.get(pg)
    print (rr.status_code)
    newSoup = BeautifulSoup(rr.text, 'html.parser')

    item_table = newSoup.find('table', id='plp-table-filter')  #this locates the table
    #print(item_table)   #works
    # i want both the header and data
    # i also want to go to each page

    if (firstFirstItem):
        for h in item_table.find_all('thead'):
            links = h.find_all('a')
        
        for l in links:
            colNames.append( l.text.strip() )

        df = pd.DataFrame(columns=colNames )
        firstFirstItem = False



    #ONCE WE GO TO THE SUBLINKED PAGE we need to set up a sub dataframe.  but once it is set up we dont need
    # to set it up again
    #each sub page can have slightly different data and could have missing columns
    firstSubItem = True

    #now need to return the body data.
    #part will be a link all other data will simply be data

    #need to find itemprop = 'sku' for part and itemprop = 'value' for dat
    ##############################################################################################
    ###########   start wtih MAIN table data scrape
    #############################################################
    for b in item_table.find_all('tbody'):
        #print (b.text.strip())
        for row in b.find_all('tr'):
            part = row.find('span', itemprop = 'sku')   #returns the part number but no link data
        # data = row.find_all('span', itemprop = 'value')   # returns all data about the item
            data = row.find_all('td')
            #print (part.text.strip())
            data_listA.append(part.text.strip())
            
            detail_link = row.find('a', class_='plp-itemlink')
            sub_link = url_pre + detail_link.get('href')
            #print(sub_link)
            dcol = 0
            loc = 0
            for d in data[1:]:
            
                colPos = 0
                strData = ''
                value = d.find_all('span' , itemprop='value')
                for v in value:
                    #print(loc, v.text)
                    if (colPos == 0 ):
                        strData = v.text
                    else:
                        strData = strData +' / '+ v.text
                    colPos += 1
                        
            # print(loc, strData)
                data_listA.append(strData)
            
                dcol += 1
                
                loc += 1
            df.loc[len(df)] = data_listA
            print (data_listA)
            data_listA=[]
            
            #########################################################################################
            ########################   EXTRACT FROM SUB PAGE STORE IN ITS OWN DF    #################
            #########################################################################################
            #get the data from the detail page associated with each part
            r1 = requests.get(sub_link)
            sub_soup = BeautifulSoup(r1.text, 'html.parser')
        
            subCol = 0
            subDataHeaders = []
            dataElementList=[]
            detail_tables = sub_soup.find_all('table', class_='plp-item-table')  #this locates the table
            for dt in detail_tables:   #loop through the list of tables
                subDataRows = dt.find_all('tr', itemprop='additionalProperty')
                for sdr in subDataRows:
                    data_Name = sdr.find('td', class_='plp-table-name left')
                    dfColName = data_Name.text.strip()
                    data_Elements = sdr.find('td', class_='plp-table-value' )   #' plp-spec-value'
                    data_element_list = data_Elements.find_all('span', itemprop = 'value')
                    dataElement = []
                    subDataHeaders.append(dfColName)
                    #some data elements have more than one piece of data,  lets make a list of them           
                    for de in data_element_list:
                        dataElement.append(de.text.strip())
                    #print (data_Name.text.strip(),dataElement)
                        
                    dataElementList.append(dataElement)
                    #add any columns then add any data elements individually
                    if (not firstSubItem):
                        #subDF.insert(length, data_Name.text.strip(), data_element_list)
                        if (dfColName in subDF.columns):
                            subDF.at[length, dfColName]= dataElement   #must use 'at' to insert a LIST at a specific location
                        else:
                            #append the column
                            dummyData=[]
                            for i in range(0,length):
                                dummyData.append('')   #since new column, fill existing records with ''
                            dummyData.append(dataElement)
                            subDF.insert(len(subDF.columns),dfColName,dummyData)

                    #  subDF.loc[length, dfColName]= dataElement   #commented this out 
        ##########################   WORKING ON ABOVE FAILS ON FAFNIR and SPLIT CRB HERE ##################
                
            if (firstSubItem):
                subDF = pd.DataFrame(columns = subDataHeaders)
                firstSubItem = False     
                length = len(subDF)
                subDF.loc[length] = dataElementList  # this is ok because this will match the columns exactly.
            #subDF.insert(len(subDF),list(zip(dataElementList)))
            length = len(subDF)
            
        # print (subDataHeaders)
        # print (dataElementList)
            print('')      

    print (subDF)
            # SI and Imperial data is separated and needs to be combined somehow.
            # not sure if each housed unit type will present data teh same way.
df_combined = pd.concat([df, subDF], axis=1)
df_combined.to_csv('scrape.csv', index=False)  