def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # getting end index as its used in lots of places
    end_idx = len(input_list) - 1
    # Find the pivot point  
    pivot = getPivot(input_list, 0, end_idx)
    # print(pivot)
    if pivot == -1:
        # Array is not rotated so just do normal binary search
        return rotated_search_recursion(input_list, number, 0, end_idx)
    # check if pivot point is already equal to value being searched for
    if input_list[pivot] == number:
        return pivot
    # if value at pivot is greater than value being searched for, then go search right, otherwise go left
    if input_list[0] <= number:
        return rotated_search_recursion(input_list, number, 0, pivot - 1)
    return rotated_search_recursion(input_list, number, pivot + 1, end_idx)


    
    pass

def getPivot(input_list, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((high-low)/2)
    # If the value on the middle is bigger than the one on the right, then thats the index point
    if mid < high and input_list[mid] > input_list[mid+1]:
        return mid
    # if value on middle is smaller than the one on the left, then the left is the pivot point
    if mid > low and input_list[mid] < input_list[mid-1]:
        return mid-1
    # else recurse until you find it
    if input_list[low] >= input_list[mid]:
        return getPivot(input_list, low, mid - 1)
    return getPivot(input_list, mid, high)
    

def rotated_search_recursion(input_list, number, start_idx, end_idx):
    if start_idx > end_idx:
        return -1
    mid = int((start_idx + end_idx) / 2)
    mid_el = input_list[mid]
    if mid_el == number:
        return mid
    if mid_el <= number:
        return rotated_search_recursion(input_list, number, mid + 1, end_idx)
    return rotated_search_recursion(input_list, number, start_idx, mid - 1)
        



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    # print(rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Complexity is O(n(log n)) since I am using binary search to find the pivot point and index of the searched value
# Space complexity is O(1) since I am not creating new data structures