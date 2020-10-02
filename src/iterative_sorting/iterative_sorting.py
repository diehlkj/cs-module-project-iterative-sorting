# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):                # * O(n), linear time
        cur_index = i                                     # * O(1), constant time
        smallest_index = cur_index                        # * O(1), constant time
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):                # * O(n), linear time
            if arr[smallest_index] > arr[j]:                        # * O(1), constant time
                smallest_index = j                                  # * O(1), constant time

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]   # * O(1), constant time

    return arr
# * Big-O Calculation  O(n) * ( O(1) + O(1) + O(n) * ( O(1) + O(1) )):
# *                    O(n) * (O(2n) + 2)
# *                    O(n^2)?

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    arr_len = len(arr)
    # ? for 'index' of 0 to length of input array
    for i in range(arr_len): # * O(n), linear time
        # ? loop again for each 'index' of 0 to length of input array - outer index - 1.
        # ? Every time 'i' increases, it limits the number of indexes in 'arr' to be looked through by 1.
        for j in range(arr_len - i - 1): # * O(n), linear time
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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
