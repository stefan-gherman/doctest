

def cyclic_rotation(string,places):
    '''
    >>> cyclic_rotation('abcde',2)
    'deabc'
    >>> cyclic_rotation('Tide',3)
    'ideT'
    >>> cyclic_rotation('Horse',-2)
    'rseHo'
    >>> cyclic_rotation('Tide',5)
    'eTid'
    >>> cyclic_rotation('Horse',-7)
    'rseHo'
    >>> cyclic_rotation('Horse',-5)
    'Horse'
    >>> cyclic_rotation('Tide',7)
    'ideT'
    '''

    if abs(places) >= len(string):
        new_places = abs(places) % len(string) 
        ''' 
        Based on some caculations it has occured that if a number larger than the lenght of the string 
        is passed, the same number of rotations as the result of places%/string lenght will occur
        
        '''
    else:
        new_places = abs(places)    
            
    #print(places)


    cycle_string = ""

    if places > 0:
        for i in range(len(string)):
            cycle_string += string[i-new_places]
    else:
        new_string = string[-1::-1]
        #print(new_string)
        for i in range(len(new_string)):
            cycle_string += new_string[i-new_places]
        #print(i ,string[i],cycle_string)
        cycle_string = cycle_string[-1::-1]

    return cycle_string

