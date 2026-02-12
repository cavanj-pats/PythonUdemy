#object_Multithreading.py

#function method
#object method.  using a class

#sample from lecture
#65 - 90 print integer and alpha character from Ascii code


from threading import *
from time import *


#class method
class Alphabets(Thread):
    def run(self):
        for i in range (65, 91):
            print (chr(i))
            sleep(0.2)


def display():
    for i in range(65, 91):
        print (chr(i))
        sleep(0.2)


#t = Thread(target=display, name='Alphabets')  #for function method
t = Alphabets()
t.start()  #start thread

for i in range(65, 91):
    print (i)
    sleep(0.2)

t.join()



#if __name__ == "__main__":