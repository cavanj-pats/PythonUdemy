#header.py



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
header = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf", # type: ignore
                      flavor='stream'  ,  #'lattice',
                      pages= pages ,
                      table_areas = ['5,800,550,750'] ,
                      flag_size = True,    
                      strip_text = '\n' ,
                      layout_kwargs = {'detect_vertical' : True} )


maxCol = 0
for ta in range(len(header)):
    if header[ta].df.shape[1] > maxCol:
        maxCol = header[ta].df.shape[1]

#maxCol += 1
firstTable = True

for t in range(len(header)):
    
    if t == 0 and firstTable:
       # header[t].df.insert(maxCol, 'Series',header[t].df[0][0])    # headerData.values[0][t]
        header[t].df.insert(maxCol,'Block_Type', header[t].df[0][1] )  #headerData.values[1][t]
        header[t].df.insert(maxCol+1,'PDF_Page', header[t].page)
        header[t].df.to_csv('tmp_header.txt' )
        firstTable = False
    else:
     #   header[t].df[maxCol]=  header[t].df[0][0]      #headerData.values[0][0]
        header[t].df[maxCol] =  header[t].df[0][1]    #headerData.values[1][0]
        header[t].df[maxCol+1] = header[t].page
        header[t].df.to_csv('tmp_header.txt', mode='a', header=False )
