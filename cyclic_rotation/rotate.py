

def cyclic_rotation(string,places):
    '''
    >>> cyclic_rotation('abcde',2)
    'deabc'
    >>> cyclic_rotation('Tide',3)
    'ideT'
    >>> cyclic_rotation('Horse',-2)
    'rseHo'
    '''


    cycle_string = ""

    for i in range(len(string)):
        if places > 0:
            cycle_string += string[i-places]
        else:
            cycle_string += string[i+places-1]
    return cycle_string

