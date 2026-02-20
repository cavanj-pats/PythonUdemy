#challenge_DS_IntegersHighestProduct.py

import array

def calcHighestProduct(arr):
    highestProduct = 0
    elements=[]

    for i in arr:
        for j in arr:
            if i != j :
                if (i * j) > highestProduct:
                    highestProduct = i*j
                    elements = [i,j]

    print(f'Highest Product: {highestProduct}, Elements: {elements}')

    """
        abdul had a smarter set of nexted loops
        x=arr[0]
        y=arr[1]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
            if arr[i]*arr[j] > x*y:
                x = arr[i]
                y = arr[j]
                # the setting of j's range assures j != i so the result will be correct.
                #mine is slightly more wasteful as it will run uncessary loops
                #whereas abdul's does not.
        return x, y
    """     
    



if __name__ == "__main__":
    #my_array = array.array('i',[2,4,6,8,3,7,9])
    my_array = array.array('i',[0, -1, -3, -5, -8 , 2, 4])
    calcHighestProduct(my_array)