#header footer testing

# headfoot.py


import camelot
import pypdfium
import csv
import pandas as pd
import re     #regex for pattern match

## seems i need to set a GlobalMaxNumColumns as some tables have more columns   Series and Block type
## need to be beyond the actual data so that it does not over write actual data that is needed
#globalMaxColumns = 25

#header  scale ('10,)
pages = '94-138, 141-180, 183-209, 213-253'

header = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf", # type: ignore
                      flavor='stream'  ,  #'lattice',
                      pages= pages , # '94-138' ,  #, 141-180, 183-209, 213-253' ,     
                      table_areas = ['5,800,550,720'] ,
                      flag_size = True,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} )

footer = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf", # type: ignore
                      flavor='stream'  , 
                      pages= pages , #'94-138' ,
                      table_areas = ['5,35,550,5'] ,
                      flag_size = False, #was True   
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} ) 
 
camelot.plot(header[0], kind = 'grid', filename='grid')
camelot.plot(footer[0], kind = 'grid', filename='grid')
camelot.plot(header[0], kind = 'text', filename='text')
camelot.plot(footer[0], kind = 'text', filename='text')

for t in range(len(header)):
   #print (header[t].page)
   print (header[t].page, header[t].df[0][0], header[t].df[0][1])

for f in range(len(footer)):
    print (footer[f].page, footer[f].df[0][0])
