"""
Explanation:
Linear search, also known as sequential search, is a simple searching algorithm that iterates through 
the elements of an array or list one by one until it finds the target element or reaches the end of the list.


Time Complexity: O(n). In the worst case, the algorithm will have to iterate through the entire array.

Space Complexity: O(1)
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target not found in the array

# Example usage:
arr = [4, 2, 9, 1, 5, 7]
target = 5
result = linear_search(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")
