def linear_search(arr, target):
    # Your code here
    for item in arr:
        if target == item:
            return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    lower = 0
    upper = len(arr) - 1
    middle = 0
    
    while lower <= upper:
        middle = int((lower + upper) / 2)
        
        if arr[middle] == target:
            return arr.index(target)
        else:
            if target > arr[middle]:
                # ? search range middle to len(arr) and repeat
                lower = middle
                
            elif target < arr[middle]:
                # ? search range 0 to middle and repeat
                upper = middle

    return -1  # not found
