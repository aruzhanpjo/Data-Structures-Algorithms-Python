#Time complexity


"""
1. Constant time O(1). 
This code snippet has a constant time complexity 
because it performs a single operation regardless of the input size.
"""
def constant_time_example(arr):
    return arr[0]


"""
#2. Linear time O(n)
In this example, the function has a time complexity of O(n) 
because it loops through the input array once.
"""
def linear_time_example(arr):
    total = 0
    for num in arr:
        total += num
    return total



"""
#3. Quadratic time O(n^2)
This code snippet has a time complexity of O(n^2) because it contains nested loops.
"""
def quadratic_time_example(arr):
    total = 0
    for i in arr:
        for j in arr:
            total += i * j
    return total



"""
#4. Logarithmic Time (O(log n)):
This example demonstrates a binary search algorithm, which has a time complexity of O(log n).
"""
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1




"""
#5. Linearithmic Time (O(n log n)):
Merge Sort is an example of an algorithm with a time complexity of O(n log n).
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


