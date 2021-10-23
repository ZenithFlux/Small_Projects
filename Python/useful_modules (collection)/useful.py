def findkey(dict, value, instance = 1):
    #This function returns the key of the entered value in dictionary dict. 
    # If multiple instances of the value is present, this will provide the key of the instance no. given.
    
    keys_list= [a for a, b in dict.items() if b == value]
    return keys_list[instance - 1]
