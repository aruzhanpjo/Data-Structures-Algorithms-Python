"""
Algorithm:
1. Compare the first two elements in the list or array.
2. If the first element is larger than the second element (for ascending order), swap them.
3. Move to the next pair of elements and repeat the comparison and swapping if necessary.
4. Continue this process until you reach the end of the list or array.

Time Complexity: O(n^2) - worst case; O(n) - best case

Space Complexity: O(1)
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps were made in the current pass
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
