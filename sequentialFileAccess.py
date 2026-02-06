# sequentional file access

#using with, you don't need to close the file when you are done using it.
with open('dataSeq.txt', 'r') as file:
    ch1 = file.read(1)
    print (ch1)
    ch2 = file.read(3)
    print (ch2)
    ch3 = file.read()
    print (ch3)
    #you can't bring the pointer back to the beginning or anywhere else.
    
