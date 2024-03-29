
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Loop through the array and check the current and next element
    if len(input_list) == 0:
        return []
    idx = 0
    while idx < len(input_list) - 1:
        # check if next element is greater
        if input_list[idx] > input_list[idx + 1]:
            temp = input_list[idx]
            input_list[idx] = input_list[idx + 1]
            input_list[idx + 1] = temp

            # Go back and check from previous value again
            idx = -1
        idx += 1
    return input_list
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])