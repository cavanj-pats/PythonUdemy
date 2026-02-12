#object_MultithreadingSemaphoreSynch.py

#achieve synchronization with Semaphore

#sort of like a lock. Maybe more like a valve
#it can allow more than one thread....

from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()




if __name__ == "__main__":
    

    l = Semaphore(2)  #1 lets one thread in.  2 lets two in

    t1 = Thread(target=display, args=('HELLO WORLD',))
    t2 = Thread(target=display, args=('you are welcome',))
    t3 = Thread(target=display, args=('0123456789',))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    #outputs mixed "raised condition"
