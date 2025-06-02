# tables.py


import camelot
import pypdfium
import csv


a = camelot.read_pdf("C:/Users/james/Downloads/10785_Solid-Block-Mounted-SRB-Catalog_LR.pdf",
                      flavor='lattice',
                      pages='94-96' ,
                      table_regions = ['25,500,560,180'] ,
                      #columns = ['35, 49, 62, 71, 79, 88, 96, 105, 104, 113, 122, 131, 139, 148, 156, 165, 173, 182, 190 '],
                      split_text = True,
                      flag_size = True,
                      strip_text = '\n' ,
                      line_scale = 50 ,
                      shift_text = ['t'],
                      copy_text =['v'],
                      layout_kwargs = {'detect_vertical' : True} )

camelot.plot(a[0], kind = 'grid', filename='grid')
camelot.plot(a[0], kind = 'text', filename='text')

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


