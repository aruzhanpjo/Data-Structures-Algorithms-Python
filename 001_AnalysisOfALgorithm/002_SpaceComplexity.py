#Space Complexity;


"""
#1. Constant Space (O(1)):
This code snippet has a constant space complexity 
because it uses a fixed amount of memory regardless of the input size.
"""
def constant_space_example(n):
    result = 0
    return result



"""
#2. Linear Space (O(n)):
In this example, the function has a space complexity of O(n) 
because it uses a data structure (list) whose size scales with the input.
"""
def linear_space_example(n):
    numbers = [i for i in range(n)]
    return numbers


"""
#3. Quadratic Space (O(n^2)):
This code snippet has a space complexity of O(n^2)
because it creates a 2D matrix of size n x n.
"""
def quadratic_space_example(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix



"""
#4. Logarithmic Space (O(log n)):
In this example, we use a recursive function that splits the problem into smaller parts. 
The space complexity is O(log n) due to the depth of the recursive call stack.
"""
def recursive_function(n):
    if n <= 1:
        return
    recursive_function(n // 2)




"""
#5. Linearithmic Space (O(n log n)):
Merge Sort, which is an O(n log n) time complexity algorithm, also has a space 
complexity of O(n log n) due to the need for auxiliary storage in the merge step.
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
