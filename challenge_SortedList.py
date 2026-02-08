# challenge Sorted List

import bisect as b


class SortedList:
    def __init__(self):
        self.mylist = list()

    def add(self, value):
        if(len(self.mylist)==0):
            self.mylist.insert(0,value)
        else:
            b.insort(self.mylist, value)

    def remove(self, value):
        self.mylist.remove(value)
    
    def search(self, key):
        return self.mylist.index(key)
        
    def insert_position(self, value):
        position = b.bisect_left(self.mylist, value)
        return position

    def display(self):
        print(self.mylist)


s1 = SortedList()
s1.add(10)
s1.add(5)
s1.add(7)
s1.display()