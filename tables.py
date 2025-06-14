# tables.py
#this will work for the solid block SRB.  there are some unique elements such as the one page with two tables
#that make this code only semi-reusable.

import camelot
import pypdfium
import csv
import pandas as pd
import re     #regex for pattern match

## seems i need to set a GlobalMaxNumColumns as some tables have more columns   Series and Block type
## need to be beyond the actual data so that it does not over write actual data that is needed
#globalMaxColumns = 25

pages = '94-138, 141-180, 183-209, 213-253'
twoTablePage = 0
#document = "https://www.timken.com/wp-content/uploads/2025/05/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf"
#https://www.timken.com/wp-content/uploads/2024/08/Mounted-Tapered-Roller-Bearing-Catalog_11477-1.pdf
#https://www.timken.com/wp-content/uploads/2023/07/SAF-Split-Block-Mounted-SRB-Catalog_11435.pdf
#https://www.timken.com/wp-content/uploads/2023/07/SAF-Split-Block-Mounted-SRB-Catalog_11435.pdf

#header  scale ('10,)
header = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='stream'  ,  #'lattice',
                      pages= pages ,
                      table_areas = ['5,800,550,720'] ,
                      flag_size = True,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} )

footer = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='stream'  , 
                      pages= pages ,
                      table_areas = ['5,35,550,5'] ,
                      flag_size = False,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} )

a = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='lattice',
                      pages=   pages,  #'94-138, 141-180, 183-209, 213-253' ,
                      table_regions = ['25,500,560,180'] ,
                      #columns = ['35, 49, 62, 71, 79, 88, 96, 105, 104, 113, 122, 131, 139, 148, 156, 165, 173, 182, 190 '],
                      split_text = False,  #was true can change back if needed
                      flag_size = True,    
                      strip_text = '\n' ,
                      line_scale = 50  ,
                      shift_text = ['t'],
                      copy_text =['v'],
                      layout_kwargs = {'detect_vertical' : True} )
maxCol = 0
for ta in range(len(a)):
    if a[ta].df.shape[1] > maxCol:
        maxCol = a[ta].df.shape[1]

maxCol += 1


#camelot.plot(a[0], kind = 'grid', filename='grid')
#camelot.plot(a[0], kind = 'text', filename='text')
#numTables = a.n   #number of tables access for 0 to n-1
firstTable = True

for t in range(len(a)):
    #headerData = header[t].df
        #a[0]df[0][2] finds the data in column 0 and row 2

        #this works but also picks up the period in 'mmin.'
    cols = a[t].df.shape[1]   # i think this is columns  [1] is columns [0] is rows
    rows = a[t].df.shape[0]
    row = 0
    for c in range(maxCol):
        if c < cols:
            dataSeries = (a[t].df)[c]   #column index 3/ might also be teh name of the column
            head = a[t].df[c][0]   #should be the column header from catalog
        
            #head = a[t].df[c][0]   #should be the column header from catalog
            for i in range(dataSeries.size):
                match = re.match('[0-9]{1,3}.[0-9]{2,3}.[0-9]{2}',dataSeries[i])
                if match:
                    position = dataSeries[i].find('.' )  #should find the first one.
                    if position != -1:
                        pos = position + 2
                        dataSeries[i]= dataSeries[i][:pos] + ' / ' + dataSeries[i][pos:]
                elif head == 'J' and i > 0:
                    #this is a bolt size
                    pos = 2   # bolt in milimeters is always two characters
                    dataSeries[i] = dataSeries[i][:pos] + 'mm  ' + dataSeries[i][pos:] + 'in.'
                elif head == 'Wt.' and i > 1:
                    position = dataSeries[i].find('.' )  #should find the first one.
                    if position != -1:
                        pos = position + 2
                        dataSeries[i]= dataSeries[i][:pos] + ' / ' + dataSeries[i][pos:]    
                else:
                    continue
                
            (a[t].df)[c] = dataSeries
        else:
            dataSeries = a[t].df[2]    #put shaft diameter
            a[t].df.insert(c,str(c), dataSeries)    #changed from str(c+1)
            head =''
        
        #header[t].df[0][0], header[t].df[0][1]
    x=0

    if t == 0 and firstTable:
        a[t].df.insert(maxCol, 'Series',header[t].df[0][0])    # headerData.values[0][t]
        a[t].df.insert(maxCol+1,'Block_Type', header[t].df[0][1] )  #headerData.values[1][t]
        a[t].df.insert(maxCol+2,'PDF_Page', a[t].page)
        a[t].df.insert(maxCol+3, "Footer", footer[t].df[0][0])
        a[t].df.to_csv('tmp_file.txt' )
        firstTable = False
    else:
        if a[t].page >= 188:
            if twoTablePage == 0:
                x = t
                twoTablePage = 1
            else:
                x= t - 1
        else:
            x = t

        a[t].df[maxCol]= header[x].df[0][0]      #headerData.values[0][0]
        a[t].df[maxCol+1] = header[x].df[0][1]    #headerData.values[1][0]
        a[t].df[maxCol+2] = a[t].page
        a[t].df[maxCol+3] = footer[x].df[0][0]
        a[t].df.to_csv('tmp_file.txt', mode='a', header=False )


#with open('tmp_file.txt', 'w') as f:
""" for i in range(len(a)):
    if i== 0:
        a[i].df.to_csv('tmp_file.txt' )
    else:
        a[i].df.to_csv('tmp_file.txt', mode='a', header=False ) """
       
 # Print first table
#print(a[0].df)
      
       
        #print(f"Index: {i}, Value: {my_array[i]}")
#        csv.writer(f, delimiter=',').writerows(a[i])


