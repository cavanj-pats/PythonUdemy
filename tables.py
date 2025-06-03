# tables.py


import camelot
import pypdfium
import csv
import pandas as pd


a = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='lattice',
                      pages='94' ,
                      table_regions = ['25,500,560,180'] ,
                      #columns = ['35, 49, 62, 71, 79, 88, 96, 105, 104, 113, 122, 131, 139, 148, 156, 165, 173, 182, 190 '],
                      split_text = False,  #was true can change back if needed
                      flag_size = True,    
                      strip_text = '\n' ,
                      line_scale = 50 ,
                      shift_text = ['t'],
                      copy_text =['v'],
                      layout_kwargs = {'detect_vertical' : True} )

camelot.plot(a[0], kind = 'grid', filename='grid')
camelot.plot(a[0], kind = 'text', filename='text')


#this works but also picks up the period in 'mmin.'
dataSeries = (a[0].df)[3]   #column index 3
for i in range(dataSeries.size):
    position = dataSeries[i].find('.' )   #should find the first one.
    if position != -1:
        pos = position + 2
        dataSeries[i]= dataSeries[i][:pos] + ' / ' + dataSeries[i][pos:]

(a[0].df)[3] = dataSeries

# Print first table
print(a[0].df)


#with open('tmp_file.txt', 'w') as f:
for i in range(len(a)):
    if i== 0:
        a[i].df.to_csv('tmp_file.txt' )
    else:
        a[i].df.to_csv('tmp_file.txt', mode='a', header=False )
       
       
       
        #print(f"Index: {i}, Value: {my_array[i]}")
#        csv.writer(f, delimiter=',').writerows(a[i])


