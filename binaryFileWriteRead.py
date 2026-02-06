#
# file access binary data to file

import struct
#need to use this module for binary conversion

#we will record football players id and name
#id = 14
#name = 'Smith'

RECORD_SIZE = 14
#when appending the file the data gets overwritten

#put in form of a function
def add_player(id, name):

    with open ('players.dat', 'ab') as file:  #append binary
        name = name.encode().ljust(10)  #limit to 10 characters 
        record = struct.pack('i10s', id, name)
        file.write(record)


def read_player(recnum):
    with open('players.dat', 'rb') as file:
        file.seek(recnum * RECORD_SIZE) # integer is 4 bytes string is 10 bytes
        record = file.read(RECORD_SIZE)
        if record:
            id, name = struct.unpack('i10s', record)
            print (f"ID: {id}, NAME: {name.decode()}")


#
add_player(14,'Smith')
add_player(16, 'Varun')
add_player(1, 'Ravi')
add_player(20, 'Kiran')

read_player(0)


# cat players.dat will show the human readable parts of the file.
#everytime this program executes, the program adds new records