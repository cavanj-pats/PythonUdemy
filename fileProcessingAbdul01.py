# file processing practice


"""
    r+.    read and write
    w+.    write and read
    a.   append
    a+ append and read

    rb - read binary
    wb - write binary
    ab - append binary
"""
"""
    ##different functions
    read()
    read(10).   # would be 10 bytes which is 10 characters
    readLine().  #reads all lines and puts in a list
    readable()
    writeable()


"""

"""
    #query cursor position
    tel()
    seak(offset)

"""

try:
    file = open('data.txt', 'r')
except Exception as e:
    print(e)
else:
    data = file.read()
    print (data)
    file.close()

print('\n')


#    also can use a with block.
with open('data.txt', 'r') as file:
    data = file.read()
    print (data)
    #you don't need to close when using this syntax.