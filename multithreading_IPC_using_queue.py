#multithreading_IPC_using_queue.py. IPC interprocessCommunication
from threading import *
from time import *
from queue import *  #bad habit better to import only what you need

q = Queue()
    
def producer(que):
    i = 1
    while True:
        que.put(i)
        print('Producer: ',i)
        sleep(0.5)
        i+=1
        if i > 11:
            break

def consumer(que):
    while True:
        x = que.get()
        print('Consumer: ', x)
        sleep(0.5)
        if x > 10:
            break

if __name__ == "__main__":
    
    t1 = Thread(target = lambda:producer(q))
    t2 = Thread(target=lambda:consumer(q))

    t1.start()
    t2.start()

    t1.join()
    t2.join