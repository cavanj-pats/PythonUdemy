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

##               ------  Tool to extract Housed unit, mostly pillow block, data from cad.timken.com
##               ------  tabulate the data in a csv for each product type
##               ------  make the underlying data searchable   

data_listA=[]
colNames=[]
navigation_List=[]
url_pre = 'https://cad.timken.com'

##############################################################################################################################
#    ^^^^^^^^^^^^^^^^^^^^^^^^^    TYPE E   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


##    Split CRB Light Pillow Blocks
#url = 'https://cad.timken.com/viewitems/split-cylindrical-roller-bearing-light-series-plum/split-cylindrical-roller-bearing-light-series-stan'
#numpages = 25   # Determine this by inspecting cad.timken.com
#fileName = 'SplitCRB_Light.csv'

#  ^^^^^^^^^^^^^^^^^      Solid Block SRB Pillow Blocks  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
##       There is a URL for each shaft lock plus two vs. four bold plus maybe other types
url = 'https://cad.timken.com/viewitems/single-concentric-solid-block-mounted-bearings/single-concentric-two-bolt-pillow-block'
numpages = 7    #adjust as required
fileName = 'SolidSRB_CL_2Bolt.csv'   #change as required


#         ^^^^^^^^^^^^^^^^^^   FAFNIR
#url = 'https://cad.timken.com/viewitems/fafnir--pillow-block-mounted-bearings/fafnir--pillow-block-mounted-bearings-eccentric-lo'
#numpages = 25    #adjust as required
#fileName = 'FafnirBHU_ecc.csv'   #change as required



#########################################################################################################################
# below works, don't believe it is needed anymore
#r = requests.get(url)
#print(r.status_code)
#soup = BeautifulSoup(r.text, 'html.parser')

#####  The below is an old technique that worked perfectly fine  ##########################
#get the number of pages we need to naviage to:  this will become an outer loop
#navigation_List.append(url)
#pages = soup.find('div', class_="plp-pagination")
#for p in pages.find_all('a'):
    #print (url_pre + p.get('href'))
#    navigation_List.append(url_pre + p.get('href'))


firstFirstItem = True
firstSubItem = True
#############################################  outer loop goes here 
##   1. For each set of tables within a product type,  top level page should be identical.  no need to check if columns exist.  Assumption
#for pg in navigation_List:


#find the range of x by inspection
for x in range(1,numpages+1):
    if (x == 1):
        rr = requests.get(url)
    else:
        pgnum = str(x)
        f_pgnum = f'{pgnum}'  #need to format in single quotes
        #query_payload = {'pagesize':'25','sortid':'1001410', 'measuresortid':'256','pagenum': f_pgnum , 'selecteduom':'1' }
        query_payload = {'pagesize':'25', 'sortid':'1001410', 'measuresortid':'256+262', 'pagenum': f_pgnum, 'selecteduom':'1'}
        rr = requests.get(url, params = query_payload)

    print (x, rr.status_code)

    newSoup = BeautifulSoup(rr.text, 'html.parser')

    item_table = newSoup.find('table', id='plp-table-filter')  #this locates the table
    #print(item_table)   #works.   Good for debugging
   
    if (firstFirstItem):
        for h in item_table.find_all('thead'):
            links = h.find_all('a')
        
        for l in links:
            colNames.append( l.text.strip() )

        df = pd.DataFrame(columns=colNames )
        firstFirstItem = False

    #ONCE WE GO TO THE SUBLINKED PAGE we need to set up a sub dataframe. 
    #  Once sub dataframe is set up we dont need to set it up again
    #  but each sub page can have slightly different data fields  and hence data
    #  firstSubItem flag was here but now we moved outside of outer loop so it won't get reset to True
    


    #need to find itemprop = 'sku' for part and itemprop = 'value' for data
    ##############################################################################################
    ###########   start wtih MAIN table data scrape
    #############################################################
    for b in item_table.find_all('tbody'):
        #print (b.text.strip())
        for row in b.find_all('tr'):
            part = row.find('span', itemprop = 'sku')   #returns the part number but no link data
            # data = row.find_all('span', itemprop = 'value')   # returns all data about the part but misses some data 
            data = row.find_all('td')    # returns row data 
            #print (part.text.strip())
            data_listA.append(part.text.strip())  # add the part to the data list
            
            detail_link = row.find('a', class_='plp-itemlink')
            sub_link = url_pre + detail_link.get('href')    #returns sublink page to be used later
            #print(sub_link)  #for debugging
            dcol = 0   #this is the data column
            loc = 0    #this is akin to row (I think)
            for d in data[1:]:
            
                colPos = 0   #within the list of Imperial / SI data if that is type of field
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
                data_listA.append(strData)   #strData is the combined Imperial / SI data
            
                dcol += 1   #move to the next data column                
                loc += 1   # i guess i used this for deguggin
            df.loc[len(df)] = data_listA   #append the completed data_listA for the row to the dataframe
           # print (data_listA)   #for debuggin
            data_listA=[]  # now that it has been appended, ok to clear the data list.
            
           

            #########################################################################################
            ########################   EXTRACT FROM SUB PAGE STORE IN ITS OWN DF    #################
            #########################################################################################
            #get the data from the detail page associated with each part
            r1 = requests.get(sub_link)
           # print (r1.status_code, 'sub link')
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
                    #    THE SUB PAGE MAY HAVE DIFFERENT FIELDS.  Need to check for missing fields and
                    #    add any Fields needed. 
                    #    Then add the data elements individually
                    #    The first data element added needs to be a empty list up until the data element 
                    #     It is empty since we are adding it, it has not been present until now.
                    #     The problem here is we need to add each piece of data versus a list of data with
                    #      Fields and Data in same exact order
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
                
            if (firstSubItem):
                subDF = pd.DataFrame(columns = subDataHeaders)
                firstSubItem = False     
                length = len(subDF)
                subDF.loc[length] = dataElementList  # this is ok because this will match the columns exactly.
            #subDF.insert(len(subDF),list(zip(dataElementList)))
            length = len(subDF)
            
        # print (subDataHeaders)
        # print (dataElementList)
            #print('')      

    #print (subDF)
            # SI and Imperial data is separated and needs to be combined somehow.
            # not sure if each housed unit type will present data teh same way.
df_combined = pd.concat([df, subDF], axis=1)
#df_combined.to_csv('scrape.csv', index=False)  
df_combined.to_csv(fileName, index=False)  