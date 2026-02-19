#challenge_DS_array_findMissingNumber.py
# array will be sorted
# there will be only one missing value


import array

def find_missing(arr):
    min = arr[0]
    max = arr[len(arr)-1]
    total = 0  #sum of the array items
    sum = 0   #sum of all numbers in range

    for x in range(min, max + 1):
        sum = sum + x  
        if x in arr:
            total += x
    
    return sum - total




if __name__ == "__main__":
    my_array = array.array('i',[1,2,3,4,5,7])
    print(f'Missing value in {my_array} is: {find_missing(my_array)}')
    
