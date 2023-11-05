"""
Algorithm:
1. Initialize an empty list as the sorted portion.
2. Repeat the following steps until the unsorted portion becomes empty:
    a. Find the minimum (or maximum) element in the unsorted portion.
    b. Swap this minimum (or maximum) element with the first element in the unsorted portion, effectively moving it to the end of the sorted portion.
    c. Shrink the unsorted portion by removing the element that has just been sorted.
3. When the unsorted portion becomes empty, the entire list is sorted.

Time complexity: O(n^2)
Space complexity: O(1)
"""

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume the current element is the minimum
        min_index = i
        
        # Find the index of the minimum element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element in the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
