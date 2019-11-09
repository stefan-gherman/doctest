

def repeat(lst):


    '''

    Returns the maximum element that occurs the most in the list

    >>> repeat([3, 3, 3, 2, 2, 2, 4, 4])
    3
    >>> repeat([2,2,2,1,1,1])
    2
    >>> repeat([32,5,21,32,5,26,5])
    5
    '''
    ordered_list = sorted(lst, reverse=True)


    freq_dict = {}

    for elem in ordered_list:
        if elem in freq_dict.keys():
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 0

    maximum = 0

    for key in freq_dict.keys():
        if freq_dict[key] > maximum:
            maximum = freq_dict[key]
            element = key

    return element







