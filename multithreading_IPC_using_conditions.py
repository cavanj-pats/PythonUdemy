#multithreading_IPC_using_condiitons.py. IPC interprocessCommunication
from threading import *
from time import *


class MyData:
    def __init__(self):
        self.data=0. #must initiatlize
        self.cv = Condition()  #cv condiiton variable

    def put(self, d):
        self.cv.acquire()
        self.cv.wait(timeout=0)
        self.data = d
        self.cv.notify()
        self.cv.release()
        sleep(0.5)

    def get(self):
        self.cv.acquire()
        self.cv.wait(timeout=0)
        x = self.data
        self.cv.notify()
        self.cv.release()
        sleep(0.5)
        return x
    
def producer(data):
    i = 1
    while True:
        data.put(i)
        print('Producer: ',i)
        i+=1
        if i > 11:
            break

def consumer(data):
    while True:
        x = data.get()
        print('Consumer: ', x)
        if x > 10:
            break

if __name__ == "__main__":
    data = MyData()
    t1 = Thread(target = lambda:producer(data))
    t2 = Thread(target=lambda:consumer(data))

    t1.start()
    t2.start()

    t1.join()
    t2.join