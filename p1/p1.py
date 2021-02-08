def volume_cube(side = None):
    if(side == None):
        raise TypeError("No parameter")

    if(side < 0):
        raise ValueError("Side is negative")

    if(isinstance(side, complex)):
        raise TypeError("Parameter is complex number")
    
    if(isinstance(side, str)):
        raise TypeError("Parameter is a string")

    return side ** 3