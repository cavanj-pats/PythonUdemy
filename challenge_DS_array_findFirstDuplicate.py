#challenge_DS_array_findFirstDuplicate.py

import array

nums = [10, 20, 13, 14, 15, 13, 17, 10, 20, 13]

def find_duplicate():
    arr = array.array('i',nums)
    result = set()

    for num in arr:
        length = len(result)
        result.add(num)
        newLen = len(result)
        if length == newLen:
            #found duplicate
            print(f'{num} is first duplicate.')
            break

    """
    ##abdul method ****************
    for n in arr:
        if n in result:
            return n
        else:
            result.add(n)
    else:
        return -1   #no duplicates found or some other error
    
    """


if __name__ == "__main__":
    find_duplicate()