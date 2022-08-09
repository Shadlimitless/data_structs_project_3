def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Start by sorting the array in descending order using merge sort algorithm
    sorted = sort(input_list)
    # Once sorted, add elements in odd indices of the sorted list to find first max number
    print(sorted)
    first = 0
    for i in range(0, len(sorted), 2):
        first = first * 10 + sorted[i]
    
    # Get elements in even indices for second number
    second = 0
    for i in range(1, len(sorted), 2):
        second = second * 10 + sorted[i]

    return [first, second]
    pass

def sort(input_list):
    # Base condition, return the array if it has less than two elements
    if len(input_list) <= 1:
        return input_list
    # Split the array into two by finding the mid index
    mid = len(input_list) // 2
    # Sort left and right of the array
    left = sort(input_list[:mid])
    right = sort(input_list[mid:])
    # Combine the two arrays to form one array
    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        # Compare elements and add the greater one first
        if left[left_idx] > right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Add any elements that are remaining into the merged array
    merged += left[left_idx:]
    merged += right[right_idx:]
    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]