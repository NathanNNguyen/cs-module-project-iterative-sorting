# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # starting at the second item, iterate until the end of the array
    for i in range(1, len(arr)):

        # the current number at the index represents the value
        # currently being sorted
        cur_num = arr[i]

        # move the current number back through the array
        # (to the 'sorted side')
        j = i

        # keep moving until: its greater than the number before it OR
        # we reach the start of array
        while j > 0 and cur_num < arr[j - 1]:
            # replace the current value and the one to left of it
            arr[j] = arr[j - 1]
            j -= 1

        # set the value of the current index to the current number
        # at this moment, J represents the new location for the curr number
        arr[j] = cur_num

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
