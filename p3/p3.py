def full_name(first_name = None, last_name = None):

    if(first_name == None or last_name == None):
        raise TypeError("One or two parameters missing")

    if(isinstance(first_name, (complex, int, float)) or isinstance(last_name, (complex, int, float))):
        raise TypeError("Parameters are not string")

    if(isinstance(first_name, list)) or (isinstance(last_name, list)):
        raise TypeError("Parameters are list")

    return first_name + " " + last_name