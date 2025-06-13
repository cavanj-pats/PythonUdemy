# tables.py


import camelot
import pypdfium
import csv
import pandas as pd
import re     #regex for pattern match

## seems i need to set a GlobalMaxNumColumns as some tables have more columns   Series and Block type
## need to be beyond the actual data so that it does not over write actual data that is needed
#globalMaxColumns = 25

#header  scale ('10,)
header = camelot.read_pdf("https://www.timken.com/wp-content/uploads/2025/05/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='stream'  ,  #'lattice',
                      pages= '94-138, 141-180, 183-209, 213-253' ,     #141-180
                      table_areas = ['5,800,550,720'] ,
                      flag_size = True,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} )

""" footer = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='stream'  , 
                      pages='94-138' ,
                      table_areas = ['5,50,550,5'] ,
                      flag_size = True,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} ) """

a = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='lattice',
                      pages=   '94-138, 141-180, 183-209, 213-253' ,
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
    headerData = header[t].df
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
        

    if t == 0 and firstTable:
        a[t].df.insert(maxCol, 'Series', headerData.values[0][t])
        a[t].df.insert(maxCol+1,'Block_Type', headerData.values[1][t])
        a[t].df.to_csv('tmp_file.txt' )
        firstTable = False
    else:
        a[t].df[maxCol]= headerData.values[0][0]
        a[t].df[maxCol+1] = headerData.values[1][0]
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


