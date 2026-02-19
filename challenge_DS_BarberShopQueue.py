#challenge_DS_BarberShopQueue.py

from collections import deque

customerq = deque(list())

def walk_in(cust):
    customerq.append(cust)
    print(f'{cust} walked in and is added to the queue')

def serviced():
    p = customerq.popleft()   #this should remove the oldest customer in teh queue
    print(f'{p} has been serviced and is no longer in the queue')
    #print(f'The queue now contains: {customerq}')


if __name__ == "__main__":
    walk_in("John")
    walk_in("James")
    walk_in("Mark")
    walk_in("Smith")    

    serviced()
    walk_in("Frank")
    serviced()

    print (customerq)