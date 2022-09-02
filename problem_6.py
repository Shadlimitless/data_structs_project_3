import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # check for len of list as defense mech
    min = 0
    max = 0
    ls_len = len(ints)
    if ls_len == 0:
        return (0, 0)
    # check for one element in list
    elif ls_len == 1:
        return (1, 1)
    else:
        # Compare first two elements to find the min and max between them
        if ints[0] > ints[1]:
            min = ints[0]
            max = ints[1]
        else:
            min = ints[1]
            max = ints[0]
        # Go through the rest of the array comparing the other values
        for i in range(2, ls_len):
            if ints[i] > max:
                max = ints[i]
            elif ints[i] < min:
                min = ints[i]
    
    return (min, max)
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")