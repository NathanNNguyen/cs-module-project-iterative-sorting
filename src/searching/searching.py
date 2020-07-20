def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1

    while end >= start:
        # get the middle point
        middle_i = (start + end) // 2

        # compare the middle point's value with the target
        # if middle == target => return True
        if arr[middle_i] == target:
            return middle_i
        
        # move start or end index closer to another
        # to shrink our search space
        else:
            if target < arr[middle_i]:
                end = middle_i - 1
            else:
                start = middle_i + 1

    return -1  # not found
