#object_MultithreadingMutex.py
#MUTEX is a method of achieving thread synchronization using a lock

from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()




if __name__ == "__main__":
    l = Lock()

    t1 = Thread(target=display, args=('HELLO WORLD',))
    t2 = Thread(target=display, args=('you are welcome',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    #outputs mixed "raised condition"
    #how to ahieve thread synchronization.  Mutex and Semaphor.  Mutex first
    # mutex is a lock