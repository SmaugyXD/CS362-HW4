def average(array = None):
    if(array == None):
        raise TypeError("No array parameter")

    if(not isinstance(array, list)):
        raise TypeError("Array is not a list")
    
    if(len(array) == 0):
        raise ValueError("There are no elements in the list")

    return sum(array) / len(array)