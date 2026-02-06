# random file access

#using with, you don't need to close the file when you are done using it.
#notice the use of 'rb' when accessing the file.
# 'b' in output will indicate data read as binary data.
with open('dataSeq.txt', 'rb') as file:
    ch1 = file.read(4)
    print (ch1)
    print (file.tell())  #will indicate the current position.
    file.seek(3,0 )    #offset, whence
    print (file.read(2))
    file.seek(2,1)    # 1 means from the current file pointer position.
    print (file.read(2))
    file.seek(-3,1)
    print (file.read(2))

    
