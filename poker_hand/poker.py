def hand(lst):
    '''
    >>> hand([1,1,1,1,1])
    'five'

    >>> hand([2,2,2,2,3])
    'four'

    >>> hand([1,1,1,2,3])
    'three'

    >>> hand([2,2,3,3,4])
    'twopairs'

    >>> hand([1,2,2,3,4])
    'onepair'

    >>> hand([1,2,3,4,6])
    'nothing'
    '''


    out = ""
    sorted_hand = sorted(lst,reverse = True)

    freq_dict = {}

    for elem in sorted_hand:
        if elem in freq_dict.keys():
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1


    maxi = 0
    more_pairs = 1
    for key in freq_dict.keys():
        if freq_dict[key] > maxi:
            maxi = freq_dict[key]
            #position = key 
        elif freq_dict[key] == maxi and maxi == 2:
            more_pairs += 1    

    

    if maxi == 5:
        out = "five"
    elif maxi == 3:
        out = "three"
    elif maxi == 2:
        if more_pairs > 1:
            out = "twopairs"    
        else:
            out ='onepair'
    elif maxi == 4:
        out = "four"
    elif maxi == 1:
        out = "nothing"    


    return out