#footer_header.py

#create a table tmp_headfoot.txt with header and footer data in it
"""  TO DO
    separate the footer text into catalog secion description and paper page number

"""






import camelot
import pypdfium
import csv
import pandas as pd


class HeaderFooter:
   
    def __init__(self, head1, head2, foot1):
        self.series = head1  # Instance attribute
        self.block_type = head2
        self.foot1 = foot1


pages = '94-138, 141-180, 183-209, 213-253'  #'187-189' #
#twoTablePage = 0
#document = "https://www.timken.com/wp-content/uploads/2025/05/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf"
#https://www.timken.com/wp-content/uploads/2024/08/Mounted-Tapered-Roller-Bearing-Catalog_11477-1.pdf
#https://www.timken.com/wp-content/uploads/2023/07/SAF-Split-Block-Mounted-SRB-Catalog_11435.pdf
#https://www.timken.com/wp-content/uploads/2023/07/SAF-Split-Block-Mounted-SRB-Catalog_11435.pdf

#header  scale ('10,)
footer = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf", # type: ignore
                      flavor='stream'  , 
                      pages= pages ,
                      table_areas = ['5,35,550,5'] ,
                      flag_size = False,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} )

header = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf", # type: ignore
                      flavor='stream'  ,  #'lattice',
                      pages= pages ,
                      table_areas = ['5,800,550,750'] ,
                      flag_size = True,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} )


maxCol = 0
for ta in range(len(footer)):
    if footer[ta].df.shape[1] > maxCol:
        maxCol = footer[ta].df.shape[1]

#maxCol += 1
firstTable = True

for t in range(len(footer)):
    if t == 0 and firstTable:
        footer[t].df.insert(maxCol,'PDF_Page', footer[t].page)
        footer[t].df.insert(maxCol+1, "Header_Page",header[t].page)
        footer[t].df.insert(maxCol+2, "Series", header[t].df[0][0])
        footer[t].df.insert(maxCol+3, "Block_Description", header[t].df[0][1])
        footer[t].df.to_csv('tmp_headfoot.txt' )
        firstTable = False
    else:
        footer[t].df[maxCol] = footer[t].page
        footer[t].df[maxCol+1] = header[t].page
        footer[t].df[maxCol+2] = header[t].df[0][0]
        footer[t].df[maxCol+3] = header[t].df[0][1]
        footer [t].df.to_csv('tmp_headfoot.txt', mode='a', header=False )