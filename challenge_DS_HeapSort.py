#challenge_DS_HeapSort.py
#this uses a heap to sort an unsorted list.


import heapq

def heapSort(elements):
    sorted_list=[]
    heapq.heapify(elements)


    for i in range(len(elements)):
        tmp = heapq.heappop(elements)
        sorted_list.append(tmp)
        
    return sorted_list


if __name__ == "__main__":
    lst=[11,22,3,14,25,16,17,28,10]
    print(f'Sorted list: {heapSort(lst)}')
